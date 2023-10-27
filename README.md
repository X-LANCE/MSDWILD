# MSDWild Dataset

> MSDWILD: MULTI-MODAL SPEAKER DIARIZATION DATASET IN THE WILD

This dataset is designed for multi-modal speaker diarization and lip-speech synchronization in the wild.

[Demo](https://x-lance.github.io/MSDWILD)

## Dataset Statistics
<img src='imgs/metrics.png' width=70% />

## Dataset Comparison
<img src='imgs/percentile_chart.png' width=70% />

Compared with other multi-modal datasets, the segment length distribution of our dataset is close to the audio-only in-the-wild diarization dataset, e.g., CALLHOME or DIHARD2.


## Labels
[rttms (all)](./rttms/all.rttm)

[rttms (few train)](./rttms/few.train.rttm)

[rttms (few val)](./rttms/few.val.rttm)

[rttms (many val)](./rttms/many.val.rttm)

## Wavs

-  [ Google Drive (7.56 GB)](https://drive.google.com/file/d/1I5qfuPPGBM9keJKz0VN-OYEeRMJ7dgpl)

md5: 0057f82daaddf2ce993d1bf0679929c4

## Video part

- [Raw Videos (Google Drive, 43.14 GB)](https://drive.google.com/file/d/1fGYcJvqCEikZpwDq_84q4Pau5qO5Was1)

The video file name corresponds to the audio file name.

- [Cropped faces (Google Drive, 14.49 GB)](https://drive.google.com/file/d/1poGOdkXway5MkQEGWTtM9U7TegLSOw54)


(For Chinese users, you can use [Baidu Link](https://pan.baidu.com/s/1hnrSKVDD9QS1bUnx4lV-Zg?pwd=t5t9) for faster downloading speech. )


Our multimodal speaker diarization baseline includes a subtask - active speaker detection. To train the active speaker detection algorithm ([TalkNet](https://github.com/TaoRuijie/TalkNet-ASD)  mentioned in our paper), we utilize 'cropped faces.' These are randomly generated from videos based on video content and rttm labels, and subsequently, manually rectified. However, if you choose not to use these resources, you can ignore the 'cropped faces.'

There are four categories of cropped-face videos:

- NS_segmentid: The cropped face does not speak throughout the video.

- SPK_segmentid: The cropped face speaks throughout the video.

- TURN_segmentid_01_starttime_turntime_endtime: The cropped face does not speak from start_time to turn_time but starts speaking from turn_time to end_time.

- TURN_segmentid_10_starttime_turntime_endtime: The cropped face speaks from start_time to turn_time but does not speak from turn_time to end_time.

Time is denoted in seconds format, and Segment_id corresponds to the cropped face video id within each video folder.



**[Updates]** Please disregard files with negative filenames (approximately 90 files).



**Note**:

* The database is **ONLY** for research purposes. 
* In response to community requests, we have uploaded a video.zip file due to some videos no longer being available online. This is to facilitate better replication of our work within the research community. These videos are solely for this purpose and must not be used otherwise. All usage must be in line with our [licensing agreement](MSDWILD_license_agreement.pdf). It's important to note that these materials may be removed at any time upon request from the original video owner.


## Baseline Code

You can easily reproduce the result by the following guide.

- **Audio-only** baseline are based on [Pyannote](https://github.com/pyannote/pyannote-audio). You can directly use [Hugging Face Edition](https://huggingface.co/pyannote/speaker-diarization). (Experiments are conducted on Pyannote ``094717b6`` and its hugging face ``3602c22f``)

- **Multi-modal** baseline are based on [TalkNet-ASD](https://github.com/TaoRuijie/TalkNet-ASD) (Pretrained models: ``msdwild.pretrained.model`` on our dataset can be downloaded from [URL](https://drive.google.com/file/d/1CdK3gRcs2pMaWB2s3X1n_0LuX6ZfQAE0)) for audio-visual realtion and [ArcFace](https://github.com/deepinsight/insightface/tree/master/recognition) for face clustering. 
    - Please add face recognition to the pipeline of [demoTalkNet.py](https://github.com/TaoRuijie/TalkNet-ASD/blob/main/demoTalkNet.py).
    - Search a best threshold from ``-0.5`` to ``0.5``.
    - If the prediction threshold is large than the best threshold, mark the corresponding frame as the active state (The minimal continuous frame is ``3``).
    - Convert the result to RTTM. 

No other post-processing methods are used.


## Baseline Result

<img src='imgs/baseline_results.png' width=70% />

## Analysis Result

You can refer to [URL](https://github.com/liutaocode/DiarizationVisualization) to visualize the dataset or your algorithm result.

<img src='imgs/via_example.png' width=70% />

## Reference

```
@inproceedings{liu22t_interspeech,
  author={Tao Liu and Shuai Fan and Xu Xiang and Hongbo Song and Shaoxiong Lin and Jiaqi Sun and Tianyuan Han and Siyuan Chen and Binwei Yao and Sen Liu and Yifei Wu and Yanmin Qian and Kai Yu},
  title={{MSDWild: Multi-modal Speaker Diarization Dataset in the Wild}},
  year=2022,
  booktitle={Proc. Interspeech 2022},
  pages={1476--1480},
  doi={10.21437/Interspeech.2022-10466}
}
```
