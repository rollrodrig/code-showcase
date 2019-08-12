## Description

FileSystem.tsx use a component inside called Folder wich implements itself with a recursive function based on json structure.

![example](example-1.png?raw=true "example")

![example](example-2.png?raw=true "example")

```json
let assets:TFile[] = [
	{
		"id": "5ca41feae249320d686cb0ca",
		"uuid": "839fbd19-55bb-11e9-abed-5ba42514e35d",
		"user_id": "5ca41feae249320d686cb0b8",
		"enabled": true,
		"assets_name": "Roll-Art-72",
		"fid": "839fbd1a-55bb-11e9-abed-5ba42514e35d",
		"fn": "rollart_1",
		"sf": 1,
		"f": [
		  {
			"fid": "839fbd1b-55bb-11e9-abed-5ba42514e35d",
			"fn": "ground",
			"sf": 0,
			"f": [
			  {
				"fid": "839fbd1c-55bb-11e9-abed-5ba42514e35d",
				"fn": "ground-0.png",
				"sf": 0,
			  },
			  {
				"fid": "839fbd1d-55bb-11e9-abed-jyjuy433",
				"fn": "ground-1.png",
				"sf": 0
			  },
			  {
				"fid": "839fbd1e-55bb-11e9-abed-asda344",
				"fn": "ground-2.png",
				"sf": 0
			  },
			  {
				"fid": "839fbd1e-55bb-11e9-abed-kiu343534",
				"fn": "ground-3.png",
				"sf": 0
			  },
			  {
				"fid": "839fbd1e-55bb-11e9-abed-45ytyjtyj",
				"fn": "ground-4.png",
				"sf": 0
			  },
			  {
				"fid": "839fbd1e-55bb-11e9-abed-hyththhyt",
				"fn": "ground-5.png",
				"sf": 0
			  }
			]
		  },
		  {
			"fid": "839fbd1f-55bb-11e9-abed-5ba42514e35d",
			"fn": "wall",
			"sf": 0,
			"f": [
			  {
				"fid": "839fbd20-55bb-11e9-abed-5ba42514e35d",
				"fn": "wall-0.png",
				"sf": 0
			  },
			  {
				"fid": "839fbd21-55bb-11e9-abed-5ba42514e35d",
				"fn": "wall-1.png",
				"sf": 0
			  },
			  {
				"fid": "839fbd22-55bb-11e9-abed-5ba42514e35d",
				"fn": "wall-2.png",
				"sf": 0
			  },
			  {
				"fid": "839fbd23-55bb-11e9-abed-5ba42514e35d",
				"fn": "wall-3.png",
				"sf": 0
			  },
			  {
				"fid": "839fbd23-55bb-11e9-abed-33fgg",
				"fn": "wall-4.png",
				"sf": 0
			  }
			]
		  },
		  {
			"fid": "839fbd24-55bb-11e9-abed-5ba42514e35d",
			"fn": "props",
			"sf": 0,
			"f": [
			  {
				"fid": "839fbd25-55bb-11e9-abed-5ba42514e35d",
				"fn": "prop-0.png",
				"sf": 0
			  },
			  {
				"fid": "839fbd26-55bb-11e9-abed-5ba42514e35d",
				"fn": "prop-1.png",
				"sf": 0
			  },
			  {
				"fid": "839fbd27-55bb-11e9-abed-5ba42514e35d",
				"fn": "prop-2.png",
				"sf": 0
			  },
			  {
				"fid": "839fbd28-55bb-11e9-abed-5ba42514e35d",
				"fn": "prop-3.png",
				"sf": 0
			  }
			]
		  }
		]
	  },
];

let entityAssets:TFile[] = [
	{
		"id": "5ca41feayyywefeca",
		"uuid": "839fbd1zzz-5ba4yyy14e35d",
		"user_id": "5ca4yyyff0d686cb0b8",
		"enabled": true,
		"assets_name": "Jim art 2019 characters",
		"fid": "839fbd1aewfwefgwg5yy5d",
		"fn": "jmart_heros_pack",
		"sf": 1,
		"f": [
		  {
			"fid": "839fbd1byyjytjtyjyjtyjt-jjty",
			"fn": "warriors",
			"sf": 0,
			"f": [
			  {
				"fid": "839fbd1c-55bb-11e9jytjyyy3432",
				"fn": "char-1.png",
				"sf": 0,
			  },
			  {
				"fid": "839fbd1c-55bjtyyyyjtyerge",
				"fn": "char-2.png",
				"sf": 0,
			  },
			  {
				"fid": "839fbjtyyyyyjyt-11e9-abed-gegerge",
				"fn": "char-3.png",
				"sf": 0,
			  },
			  {
				"fid": "839frthrhrthtrhed-gegyyyyrge",
				"fn": "char-4.png",
				"sf": 0,
			  },
			  {
				"fid": "839fbd1c-55bhtrhrhryygerge",
				"fn": "char-5.png",
				"sf": 0,
			  },
			]
		  },
		  {
			"fid": "839fbgggherheabed-ujjjtyj",
			"fn": "mages",
			"sf": 0,
			"f": [
			  {
				"fid": "839fgewgggweged-wwgwgw",
				"fn": "char-1.png",
				"sf": 0
			  },
			  {
				"fid": "839fbwefewfbb-11e9-abed-kykyu",
				"fn": "char-2.png",
				"sf": 0
			  },
			  {
				"fid": "839fbd21-55bkyukkyued-kygggyu",
				"fn": "char-3.png",
				"sf": 0
			  },
			  {
				"fid": "839fbd21-htrhhrted-kykyu",
				"fn": "char-4.png",
				"sf": 0
			  },
			]
		  },
]
```