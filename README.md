# isogeo-2-arcgis

Desktop collection of utilities to fill-full ArcGIS metadata from Isogeo.

**Still in study**

## Requirements

* ArcGIS 10.3.x + 
* Python 2.7.9+
* [Isogeo Python SDK](https://github.com/Guts/isogeo-api-py-minsdk)
* [Arcpy Metadata Editor](https://github.com/ucd-cws/arcpy_metadata)
* Proxy basic authentication to *.api.isogeo.com (not NTLM)

## Specifications

### User scenario

1. Editor fillfulls its metadata on [Isogeo](https://github.com/Guts/isogeo-api-py-minsdk) ;
2. Administrator shares metadata to the isogeo-2-arcgis application
3. Parameters to set:
	* API oAuth2 id/secret,
	* proxy url and access,
	* absolute path to data store (folder structure or sde connection file),
	* which field will be fillfull or not,
	* option to replace existing information,
4. Perform a matching test: program tries to establish match between data and metadata. Fields used:
	* name: technical filename/table name
	* path: absolute path to the dataset
5. User review the match report and edit if needed
6. Launch the synchronization from Isogeo to ArcGIS according to preferences

### Features

- [] use oAuth2 authentication to the Isogeo API
- [] flexible automatic match options
- [] option to override with manual match
- [] option to pick which metadata field to replace if existing
- [] keep a simple history


### Distribution

This utility should be distributed as:

* independant scripts - mandatory
* ArcToolbox with basic UI
* Esri Add-in with complete UI integration
