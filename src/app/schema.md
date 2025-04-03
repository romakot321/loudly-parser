Authorization: Bearer {token}

# POST https://soundtracks.loudly.com/ai/vega/bundles
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb
Content-Disposition: form-data; name="bundle_type"

ADVANCED
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb
Content-Disposition: form-data; name="genre"

Deep House
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb
Content-Disposition: form-data; name="duration"

128
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb
Content-Disposition: form-data; name="instruments[]"

DRUMS
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb
Content-Disposition: form-data; name="instruments[]"

BASS
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb
Content-Disposition: form-data; name="instruments[]"

PERCUSSION
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb
Content-Disposition: form-data; name="instruments[]"

SYNTH
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb
Content-Disposition: form-data; name="instruments[]"

STRINGS
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb
Content-Disposition: form-data; name="genre_blend"

Techno
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb
Content-Disposition: form-data; name="energy"

original
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb
Content-Disposition: form-data; name="structure_id"

2
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb
Content-Disposition: form-data; name="bpm"

125
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb
Content-Disposition: form-data; name="key_root"

E
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb
Content-Disposition: form-data; name="key_quality"

minor
------geckoformboundary913924e5d85a88021edaef9c1bb3c4fb--


## Response
{"id":"eaaae012-1ea7-49f2-9b89-fbb9040d0bca","created_at":"2025-04-03T11:04:42+0200","formula":{"genre":"Deep House","genre_blend":"Techno","bpm":125,"key":"E-minor","instruments":["DRUMS","BASS","PERCUSSION","SYNTH","STRINGS"],"duration":128,"energy":"original","structure_id":2,"prompt":null,"extra_params":null,"user_audio":null,"entropy":null},"type":"ADVANCED","capacity":3,"is_finished":false,"vega_songs":[],"is_preview":false,"errors":[]}


# GET https://soundtracks.loudly.com/ai/vega/bundles/eaaae012-1ea7-49f2-9b89-fbb9040d0bca?limit=10

## Response
{"id":"eaaae012-1ea7-49f2-9b89-fbb9040d0bca","created_at":"2025-04-03T11:04:42+0200","formula":{"bpm":125,"key":"E-minor","genre":"Deep House","energy":"original","prompt":null,"entropy":null,"duration":128,"user_audio":null,"genre_blend":"Techno","instruments":["DRUMS","BASS","PERCUSSION","SYNTH","STRINGS"],"extra_params":null,"structure_id":2},"type":"ADVANCED","capacity":3,"is_finished":false,"vega_songs":[{"id":"b281c2f4-106a-11f0-a9e4-06b28167ed55","title":"Twilight Groove","duration":129000,"music_file_path":"https:\/\/d28l47h1uhvbhl.cloudfront.net\/assets\/music_file\/01d5134d-ad76-4508-ba21-58d2db63b457.mp3?cb=20250403110454","wav_file_path":"https:\/\/d28l47h1uhvbhl.cloudfront.net\/assets\/song_wav\/b85ac838-b0d6-4421-9ca2-b4467def5034.json?cb=20250403110454","created_at":"2025-04-03T11:04:49+0200","is_in_library":false,"xml_file_path":"https:\/\/d28l47h1uhvbhl.cloudfront.net\/assets\/song_xml\/1c11ea48-e414-4102-8931-6256875ea3d5.xml?cb=20250403110454","formula":{"bpm":125,"key":"E-minor","genre":"Deep House","energy":"original","prompt":null,"entropy":null,"duration":128,"user_audio":null,"genre_blend":"Techno","instruments":["DRUMS","BASS","PERCUSSION","SYNTH","STRINGS"],"extra_params":null,"structure_id":2},"is_preview":false}],"is_preview":false,"errors":[]}


# POST https://soundtracks.loudly.com/ai/vega/bundles

------geckoformboundaryb02865f069a7e2e9c238355d71873c1c
Content-Disposition: form-data; name="bundle_type"

ADVANCED
------geckoformboundaryb02865f069a7e2e9c238355d71873c1c
Content-Disposition: form-data; name="genre"

Techno
------geckoformboundaryb02865f069a7e2e9c238355d71873c1c--

## Response
{"id":"e20209e5-d6a3-430e-aa42-7d2befc8b540","created_at":"2025-04-03T11:18:15+0200","formula":{"genre":"Techno","genre_blend":null,"bpm":null,"key":null,"instruments":null,"duration":null,"energy":null,"structure_id":null,"prompt":null,"extra_params":null,"user_audio":null,"entropy":null},"type":"ADVANCED","capacity":3,"is_finished":false,"vega_songs":[],"is_preview":false,"errors":[]}


# GET https://soundtracks.loudly.com/ai/vega/bundles/e20209e5-d6a3-430e-aa42-7d2befc8b540?limit=10

## Response
{"id":"e20209e5-d6a3-430e-aa42-7d2befc8b540","created_at":"2025-04-03T11:18:15+0200","formula":{"bpm":null,"key":null,"genre":"Techno","energy":null,"prompt":null,"entropy":null,"duration":null,"user_audio":null,"genre_blend":null,"instruments":null,"extra_params":null,"structure_id":null},"type":"ADVANCED","capacity":3,"is_finished":false,"vega_songs":[],"is_preview":false,"errors":[]}

{"id":"e20209e5-d6a3-430e-aa42-7d2befc8b540","created_at":"2025-04-03T11:18:15+0200","formula":{"bpm":null,"key":null,"genre":"Techno","energy":null,"prompt":null,"entropy":null,"duration":null,"user_audio":null,"genre_blend":null,"instruments":null,"extra_params":null,"structure_id":null},"type":"ADVANCED","capacity":3,"is_finished":false,"vega_songs":[],"is_preview":false,"errors":[]}


# POST https://soundtracks.loudly.com/oauth/v2/token
client_id=1_20k8sb2pv8kk0kck04ogcwcwc0cwok80s08o40okso0s0c0w4k&grant_type=refresh_token&refresh_token=def50200255d83ada319f33c7ff1d8eeb3e027cfd3679389ad81de99ddf085225d6357d222d728edd5bbe84b66b56f9cdc83b5451c2f3648d5b2cb98dbd3df67e91a8bf89e98777524ba0114e833a2907493a556c81de0ace0969a071d48f526f24960cec7b8c300552f799d8a5f7897e5aa604b4f7af4c9c3eeb8bdf4aa9134a019a91420b69ccca761719d42f6cdf6d29a5b9ed11c8464ca60e24c21f3249f6822f5dc64b61810f2be5fca15339637a85f15f69953cfdd22284d2dd5e463709603474ab12198cf6d04ad6dd0ba3065ea8c4f57883aefd3e75866097f5c587e8c3041e1d9f4ce42ed8e4f213ce80990d0d36c459f49ac5fdd95471892cc9059ba4c19a924db758da05abe3832e7ace7a14758b8199d34d39066e76fcab685065dd63ef7d20133111d71643589dbd2fbf59a6940063b99790f9170794f3a72f8b88a9833a4a1a324fcaf1cc589c9d8037e0dc299b4a74d4618f6c0e0216801d79c433b17ae1908c18fa245c00f6d84ffb1eed789d667af3bad53f083ef16c053d17e72375a571ba489

## Response
{"token_type":"Bearer","expires_in":3600,"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJDb3JlIiwianRpIjoiNDRmNGZmMmE0NjdiOTg0YmM3NWQxZDg1NzQ0ZjU4OWViZThlYjI5MTE1MTJlOTUxYzQ2MmNkODRmYWFjMTRiZTM1ZDFhZTZhZTc0OWM2Y2MiLCJpYXQiOjE3NDM2NzQ2NjkuNzYwMTI2LCJuYmYiOjE3NDM2NzQ2NjkuNzYwMTMxLCJleHAiOjE3NDM2NzgyNjkuNzUxOTcsInN1YiI6ImUxZTc1ODRjLTBiZDktMTFmMC1hOWU0LTA2YjI4MTY3ZWQ1NSIsInNjb3BlcyI6W119.QBer9KhmlBdmsKszD2PDKsnrH4mveHAH8YxgxkfQzq3pk2P8jZDUg4tLqD8oOHk2xcsWRTrrilA_8sQQuiPVnSkv0RSt176Volomf2mMec2yFjCD815l7KYRTfjGzsIcr1MKDhe86iWdLdqspx5i2NF5Oc5YNXyzegilxufYMIRKXW9kV_fi_SQjA7fHiwOD6aiMe6XsIQfyDSfjUhr_hotHHgH4-uMU4yzAP1AgELsGMAL71RVJRhiA5e9XROrv3l7yPI_bQan_4WDCUvNKBK6E-eTnl653CDdoAeaAdiT7FvuwDCDc82_gdmNuzPi-x4IoS1qUoctd_2hwmMBgOQ","refresh_token":"def502004c763507d01c344949d1681c4db4a23fb8f59eef6324a2c4328616120cb7a42058e676bcd82b87093767da438ad722e55af1e33c83a38c8b1dc1feb04e2c2933cf9c5420bc4ec3a393ab2ed2722f70797c26a1fdfc8ef0ff7b20d939cad1335abe4696fdcde01f921d836bf968a0858ef8b28ddf3667b98583e45acdc24e595edddf3c0f22223ab3bcfaae0a0c86b8b136f7e5e1c95dbe2cfc977ba84669553592d51b9882e1ad7cdd3f1193db163a3b46f2aaa07aefa10b8662753293a6f28925b45b9405bd79a1111e5a2b161153cfb97ed7fd660748759d95d1c5220873c7108963a62531c1768ce5b4d6fd9ffa97b7e595d272953c946effce29ad5e5d7ff316d048e22d555ef49a58b9fe4745b5d739d59f7c85fd91f539f1ca0c283b1599d0f3d6e2d73950a7afc3d164b56cd435a1e3cc1e724332bbcea9ca5e5731473deff34497e8a91072abf0d2ffed2f8a344cd9a476e62f30f124706ae98596642533eed1f3c25f5dc505b758e038af55bd7cc2c8fb0a14b70670a46a19a82a447b7ff3f3b5"}


# POST https://soundtracks.loudly.com/ai/vega/bundles
Content-Type multipart/form-data; boundary=----geckoformboundary1df53d6d5edbc2f44490898c5956fef8

------geckoformboundary1df53d6d5edbc2f44490898c5956fef8
Content-Disposition: form-data; name="bundle_type"

TEXT2MUSIC
------geckoformboundary1df53d6d5edbc2f44490898c5956fef8
Content-Disposition: form-data; name="prompt"

Michael Jordan sign Russian anthem
------geckoformboundary1df53d6d5edbc2f44490898c5956fef8--


## Response
{"id":"0027c8b5-7a7e-46bb-9b95-b0c6db08b27e","created_at":"2025-04-03T12:04:31+0200","formula":{"genre":"Alternative Hip Hop","genre_blend":null,"bpm":null,"key":null,"instruments":null,"duration":null,"energy":null,"structure_id":null,"prompt":"Michael Jordan sign Russian anthem","extra_params":null,"user_audio":null,"entropy":null},"type":"TEXT2MUSIC","capacity":3,"is_finished":false,"vega_songs":[],"is_preview":false,"errors":[]}


# GET https://soundtracks.loudly.com/ai/vega/bundles/0027c8b5-7a7e-46bb-9b95-b0c6db08b27e?limit=10

## Response

{"id":"0027c8b5-7a7e-46bb-9b95-b0c6db08b27e","created_at":"2025-04-03T12:04:31+0200","formula":{"bpm":null,"key":null,"genre":"Alternative Hip Hop","energy":null,"prompt":"Michael Jordan sign Russian anthem","entropy":null,"duration":null,"user_audio":null,"genre_blend":null,"instruments":null,"extra_params":null,"structure_id":null},"type":"TEXT2MUSIC","capacity":3,"is_finished":false,"vega_songs":[{"id":"0f2dbaba-1073-11f0-a9e4-06b28167ed55","title":"Surreal Symphony","duration":191000,"music_file_path":"https:\/\/d28l47h1uhvbhl.cloudfront.net\/assets\/music_file\/6b9297e2-0ba3-42f9-b552-5edcb1301202.mp3?cb=20250403120444","wav_file_path":"https:\/\/d28l47h1uhvbhl.cloudfront.net\/assets\/song_wav\/052daae5-d30b-4631-93c1-6c966015bf19.json?cb=20250403120444","created_at":"2025-04-03T12:04:41+0200","is_in_library":false,"xml_file_path":"https:\/\/d28l47h1uhvbhl.cloudfront.net\/assets\/song_xml\/b84c95eb-c4be-4e37-bf72-a41974ad0982.xml?cb=20250403120444","formula":{"bpm":null,"key":null,"genre":"Alternative Hip Hop","energy":null,"prompt":"Michael Jordan sign Russian anthem","entropy":null,"duration":null,"user_audio":null,"genre_blend":null,"instruments":null,"extra_params":null,"structure_id":null},"is_preview":false}],"is_preview":false,"errors":[]}


# GET https://soundtracks.loudly.com/users/limits

## Response
{"reset_data":{"current_reset_date":"2025-03-30","next_reset_date":"2025-04-30","reset_in_days":26},"usage_data":{"download_song":{"total":500,"used":0,"available":500,"top_up":null},"download_stems":{"total":20,"used":0,"available":20,"top_up":{"total":0,"used":0,"available":0}},"download_sample_pack":{"total":20,"used":0,"available":20,"top_up":{"total":0,"used":0,"available":0}},"generate_vega_song":{"total":3000,"used":9,"available":2991,"top_up":null},"export_studio_song":{"total":80,"used":0,"available":80,"top_up":null},"submit_release":{"total":20,"used":0,"available":20,"top_up":null},"upload_audio":{"total":100,"used":0,"available":100,"top_up":null}}}
