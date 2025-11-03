import argparse
from src.extract import extract_sections
from src.keypoints import pick_top_sections
from src.summarizer import make_slide_data
from src.visuals import make_visuals
from src.slides_builder import build_pptx
from src.tts import generate_audio
from src.video_maker import make_video

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--outdir', default='outputs')
    parser.add_argument('--num-slides', default=8, type=int)
    args = parser.parse_args()

    sections = extract_sections(args.input)
    candidates = pick_top_sections(sections, top_n=args.num_slides)
    slides = make_slide_data(candidates)
    make_visuals(slides, outdir=args.outdir)
    build_pptx(slides, outdir=args.outdir)
    generate_audio(slides, outdir=args.outdir)
    make_video(slides, outdir=args.outdir)

if __name__ == '__main__':
    main()
