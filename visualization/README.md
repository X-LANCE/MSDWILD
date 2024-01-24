# Visualization
The purpose of this document is to explain how to visualize the location of faces and the corresponding audio files.


The main process of visualization involves converting CSV facial data and RTTM duration information into a JSON file supported by the VIA (VGG Image Annotator) tool. Due to the constraints of the annotation tool, it's important to note that the JSON file contains absolute paths, which means that it is necessary to regenerate the JSON file each time when switching to a different machine.

## Download

Please download and unzip the files to the default path: `RELEASED_dark_labels`.

The content of the folder is like : `00001.csv`, `00001.mp4`,....

<details>
    <summary>Download URL</summary>
    
    Google Drive: https://drive.google.com/file/d/1--rqm3AKjOI9q_iNgVUD_eC2u1m4OQHW

    Baidu Drive: https://pan.baidu.com/s/1YpLMdCAcV0eG8fHmYf_lkw?pwd=msdb

    Quark Drive: https://pan.quark.cn/s/7d6332d177b9, password:5v8a
</details>


## Steps
To generate the result, just run:

```
python convert_to_mp4_with_faces.py
```

Args:

* rttm_per_file: RTTM files for each individual file
* original_mp4_files: Original video files and Darklabel csv files.
* mp4_files_with_faces: Videos with visualized faces (including face ID and bounding boxes)
* json_per_file: Visualization output (JSON files) by [VIA](https://www.robots.ox.ac.uk/~vgg/software/via/)

You can keep them at their default values.

## Preview
Open `via_video_annotator_3.0.11.html` and import an individual JSON file from the `json_per_file` directory.

## Sample Image

![](one_sample.png)

The audio ID is the same as the Face ID, starting from zero. The off-screen voice still starts with an "h" prefix, and the content of the RTTM file is consistent with that of the homepage.

For further reference, see: [DiarizationVisualization](https://github.com/liutaocode/DiarizationVisualization)
