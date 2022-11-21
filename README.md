# MSDWild Dataset

> MSDWILD: MULTI-MODAL SPEAKER DIARIZATION DATASET IN THE WILD


[Demo](https://x-lance.github.io/MSDWILD)

<img src='imgs/metrics.png' width=70% />


This dataset is designed for multi-modal speaker diarization and lip-speech synchronization in the wild.

## Labels
[rttms (all)](./rttms/all.rttm)

[rttms (few train)](./rttms/few.train.rttm)

[rttms (few val)](./rttms/few.val.rttm)

[rttms (many val)](./rttms/many.val.rttm)

## Wavs
- From Baidu Disk [ Download (8.1 GB)](https://pan.baidu.com/s/1DHIOUEuQpqJ5z9voaDBZwQ?pwd=mbc2) 

- From Google Drive [ Download (8.1 GB)](https://drive.google.com/file/d/1I5qfuPPGBM9keJKz0VN-OYEeRMJ7dgpl)

md5: 0057f82daaddf2ce993d1bf0679929c4

## Video part

The video part includes ``cropped videos`` and corresponding talking faces: ``mp4s``. If you want to use this part, [a license agreement](MSDWILD_license_agreement.pdf) must first be signed and sent to [Administration](mailto:msdwild@163.com) with your **institutional** account.

**Note**:

* The database is **ONLY** for research purposes. 
* The copyright of the video belongs to the original author, if you have any questions, please contact us ([email](mailto:msdwild@163.com)).
* You will get response in a week. (Usually in three days. Emails are sometimes undeliverable. If you do not receive our message, please contact us again.)


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
