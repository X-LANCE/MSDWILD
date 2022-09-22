# MSDWild Dataset

> MSDWILD: MULTI-MODAL SPEAKER DIARIZATION DATASET IN THE WILD 

[Demo](https://x-lance.github.io/MSDWILD)

![](imgs/metrics.png)

## Labels
[rttms (all)](./rttms/all.rttm)

[rttms (few train)](./rttms/few.train.rttm)

[rttms (few val)](./rttms/few.val.rttm)

[rttms (many val)](./rttms/many.val.rttm)

## Wavs
[Download (8.1 GB)](https://pan.baidu.com/s/1DHIOUEuQpqJ5z9voaDBZwQ?pwd=mbc2) password: mbc2 

md5: 0057f82daaddf2ce993d1bf0679929c4

## Video part

The video part includes cropped videos and corresponding talking faces. If you want to use this part, [a license agreement](MSDWILD_license_agreement.pdf) must first be signed (no students) and sent to [Administration](mailto:msdwild@163.com).

**Note**:

* The database is **ONLY** for research purposes. 
* The copyright of the video belongs to the original author, if you have any questions, please contact us ([email](mailto:msdwild@163.com)).


## Baseline Code

Codes will be released, but there is no timeline for this. We think you can easily reproduce the result by the following guide.

Audio-only baseline are based on [Pyannote](https://github.com/pyannote/pyannote-audio). You can directly use [Hugging Face Edition](https://huggingface.co/pyannote/speaker-diarization).

Multi-modal baseline are based on [TalkNet-ASD](https://github.com/TaoRuijie/TalkNet-ASD) for audio-visual realtion and [ArcFace](https://github.com/deepinsight/insightface/tree/master/recognition) for face clustering. 


If you have any other questions, feel free to contact [Tao Liu](mailto:liutaw@sjtu.edu.cn).

## Baseline Result

![](imgs/baseline_results.png)

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
