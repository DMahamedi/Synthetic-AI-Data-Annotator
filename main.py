import config
from image_collection.get_images_with_oak import collect_data
from image_collection.load_from_video import get_images_from_video
from annotating.annotate_data import annotate_images
from annotating.review_annotations import filter_annotations
from annotating.relabel_outputs import rewrite_annotation_class_id


def main():

    if config.CREATE_IMAGES and not config.USE_EXISTING_VIDEO:
        collect_data(
            config.NEW_CLASS_NAME, config.CLASS_TYPE, config.CLASS_ID,
            config.NUM_FRAME_SAMPLES, config.IMGSZ_W, config.IMGSZ_H
        )
    elif config.CREATE_IMAGES:
        get_images_from_video(config.VIDEO_PATH, config.NEW_CLASS_NAME, config.CLASS_ID)

    if config.ANNOTATE_IMAGES and not config.ANNOTATE_NEW_CLASS_ID:
        annotate_images(config.NEW_CLASS_NAME, config.YOLO_MODEL, config.CLASS_ID)
    elif config.ANNOTATE_IMAGES and config.ANNOTATE_NEW_CLASS_ID:
        annotate_images(config.NEW_CLASS_NAME, config.YOLO_MODEL, config.CLASS_ID, config.NEW_CLASS_ID)
    
    if config.FILTER_ANNOTATIONS:
        filter_annotations(config.NEW_CLASS_NAME)

    if config.RELABEL_ANNOTATION_CLASS_ID:
        rewrite_annotation_class_id(config.NEW_CLASS_NAME, config.NEW_CLASS_ID)

if __name__ == "__main__":
    main()