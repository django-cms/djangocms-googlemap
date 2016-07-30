/*
 * Copyright https://github.com/divio/djangocms-googlemap
 */

var djangocms = window.djangocms || {};

/**
 * Generates Google Map instances from plugins.
 *
 * @class GoogleMap
 * @namespace djangocms
 */

djangocms.GoogleMap = {

    options: {
        container: '.djangocms-googlemap-container'
    },

    /**
     * Initializes all Google Map instances.
     *
     * @method init
     * @private
     * @param {Object} opts overwrite default options
     */
    init: function init(options) {
        var that = this;
        var options = $.extend(true, {}, this.options, options);

        // loop through every instance
        var containers = $(options.container);
        containers.each(function (index, container) {
            that._loadMap($(container));
        });
    },

    /**
     * Loads a single Google Map instance provided by ``init``.
     *
     * @method _loadMap
     * @private
     * @param {jQuery} instance jQuery element used for initialization
     */
    _loadMap: function _loadMap(instance) {
        var that = this;
        var container = instance;
        var data = container.data();

        var options = {
            zoom: data.zoom,
            mapTypeId: google.maps.MapTypeId.ROADMAP, /* ROADMAP, SATELLITE, HYBRID or TERRAIN */
            scrollwheel: data.scrollwheel,
            disableDoubleClickZoom: data.double_click_zoom,
            draggable: data.draggable,
            keyboardShortcuts: data.keyboard_shortcuts,
            panControl: data.pan_control,
            zoomControl: data.zoom_control,
            streetViewControl: data.street_view_control,
            styles: data.style,
            center: { lat: 46.94708, lng: 7.445975 }, // default to switzerland;
        };


        var marker_tags = container.find('.djangocms-googlemap-marker');
        var markers = [];
        var promises = [];

        var map = new google.maps.Map(container[0], options);

        jQuery.each(marker_tags, function(index, marker) {
            var promise = new Promise(function(resolve, reject) {
                data = jQuery(marker).data();
                markers[index] = data;

                // latitute or longitute have presedence over the address when provided
                // inside the plugin form
                if (data.lat.length && data.lng.length) {
                    latlng = {lat: parseFloat(data.lat), lng: parseFloat(data.lng)};
                    markers[index]['latlng'] = latlng;
                } else {
                    // load latlng from given address
                    var geocoder = new google.maps.Geocoder();
                    geocoder.geocode({address: data.address}, function (results, status) {
                        // check if address can be found if not show default (var latlng)
                        if (status == google.maps.GeocoderStatus.OK) {
                            latlng = results[0].geometry.location;
                            markers[index]['latlng'] = latlng;
                            resolve(markers[index]);
                        }
                    });
                }
            });
            promises.push(promise);

        });

        var result = Promise.all(promises);
        result.then(function() {
            markers.forEach(function(marker, index) {
                // center on first marker
                if (index == 0) {
                    map.setCenter(marker.latlng);
                }
                that.addMarker(map, marker);
            });
        })


    },

    /**
     * Adds a marker to a Google Map instance.
     *
     * @method _loadMap
     * @param {jQuery} map ``google.maps.Map`` instance
     * @param {jQuery} data the data objects from a Google Map Location instance
     */
    addMarker: function addMarker(map, data) {
        var infoWindow;
        var that = this;
        var windowContent = '';
        var marker_properties = {
            'position': data.latlng,
            'map': map,
            'title': data.title
        };

        // add custom marker icon
        if (data.marker_icon) {
            marker_properties["icon"] = data.marker_icon;
        }

        var marker = new google.maps.Marker(marker_properties);

        if (data.show_infowindow) {
            // prepare info window
            if (data.title) {
                windowContent += '<h2>' + data.title + '</h2>';
            }

            windowContent += data.address;

            if (data.info_content) {
                windowContent += '<br /><em>' + data.info_content + '</em>'
            }

            infowindow = new google.maps.InfoWindow({
                content: windowContent
            });

            // show info window
            infowindow.open(map, marker);

        }

        // register click handler if the user has closed the window to reopen it
        google.maps.event.addListener(marker, 'click', (function (marker) {
            return function () {
                // reposition map
                map.setCenter(data.latlng);
                if (data.show_infowindow) {
                    infowindow.open(map, marker);
                }
                marker.setAnimation(google.maps.Animation.BOUNCE);
                setTimeout(function () { marker.setAnimation(null); }, 750);
            }
        })(marker));


    }

};

// initializes all occuring Google Map plugins at once.
djangocms.GoogleMap.init();
