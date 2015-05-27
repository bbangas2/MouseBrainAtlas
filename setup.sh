CSD181=/oasis/projects/nsf/csd181/yuncong

export PYTHONPATH=$CSD181/caffe/python:$CSD181/opencv/release/lib/python2.7/site-packages:$PYTHONPATH

export DATASET_VERSION=2015

export LD_LIBRARY_PATH=/opt/python/lib:$LD_LIBRARY_PATH:$CSD181/KDU74_Demo_Apps_for_Linux-x86-64_140513:$CSD181/opencv/release/lib
export PATH=/oasis/projects/nsf/csd181/yuncong/virtualenv-1.9.1/yuncongve/bin:$PATH:$CSD181/KDU74_Demo_Apps_for_Linux-x86-64_140513
#source /opt/intel/composer_xe_2013_sp1.2.144/bin/compilervars.sh intel64

export GORDON_SECTIONDATA_DIR=$CSD181/DavidData2015sections
export GORDON_REPO_DIR=$HOME/Brain
export GORDON_RESULT_DIR=$CSD181/DavidData2015results
export GORDON_LABELING_DIR=$CSD181/DavidData2015labelings
export GORDON_SLIDEDATA_DIR=$CSD181/DavidData2015slides
export GORDON_NDPIRAW_DIR=$CSD181/DavidData2015ndpi
export GORDON_NDPI_DIR=$CSD181/DavidData2015ndpiRenamed
#export GORDON_AUTOGEN_MASK_DIR=$GORDON_SDATA_DIR/autogen_masked_x0.3125
#export GORDON_AUTOGEN_BBOX_DIR=$GORDON_SLIDEDATA_DIR/autogen_bboxes
#export GORDON_CORRECTED_MASK_DIR=$GORDON_SLIDEDATA_DIR/corrected_masked_x0.3125
#export GORDON_CORRECTED_BBOX_DIR=$GORDON_SLIDEDATA_DIR/corrected_bboxes
export GORDON_NDPISPLIT_PROGRAM=$CSD181/ndpisplit

export MSNAKES_PATH=$GORDON_REPO_DIR/pipeline_scripts/preprocess/morphsnakes

export LOCAL_SLIDEDATA_DIR=$HOME/DavidData2015slides
export LOCAL_SECTIONDATA_DIR=$HOME/DavidData2015sections2
export LOCAL_REPO_DIR=$HOME/Brain
export LOCAL_RESULT_DIR=$HOME/DavidData2015results
export LOCAL_LABELING_DIR=$HOME/DavidData2015labelings
#export LOCAL_AUTOGEN_MASK_DIR=$LOCAL_SLIDEDATA_DIR/autogen_masked_x0.3125
#export LOCAL_AUTOGEN_BBOX_DIR=$LOCAL_SLIDEDATA_DIR/autogen_bboxes
#export LOCAL_CORRECTED_MASK_DIR=$LOCAL_SLIDEDATA_DIR/corrected_masked_x0.3125
#export LOCAL_CORRECTED_BBOX_DIR=$LOCAL_SLIDEDATA_DIR/corrected_bboxes
