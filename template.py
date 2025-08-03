import argparse
import sys

from tclogger import logger, copy_folder, rename_texts


class TemplateArgParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_argument(
            "-s",
            "--source",
            type=str,
            help="source folder",
        )
        self.add_argument(
            "-t",
            "--target",
            type=str,
            required=True,
            help="target folder",
        )
        self.add_argument(
            "-n",
            "--name",
            type=str,
            required=True,
            help="package name",
        )
        self.add_argument(
            "-d",
            "--description",
            type=str,
            required=True,
            help="package description",
        )
        self.add_argument(
            "-v",
            "--version",
            type=str,
            default="0.1",
            help="package version",
        )

    def parse_args(self):
        self.args, self.unknown_args = self.parse_known_args(sys.argv[1:])
        return self.args


includes = []
excludes = [__file__, ".git"]


def main(args: argparse.Namespace):
    miss_msg = "× Missing arg:"

    if not args.source:
        logger.warn(f"{miss_msg} -s (--source)")
    else:
        source = args.source

    if not args.target:
        logger.warn(f"{miss_msg} -t (--target)")
        return
    else:
        target = args.target

    if not args.name:
        logger.warn(f"{miss_msg} -n (--name)")
        return

    if not args.version:
        logger.warn(f"{miss_msg} -v (--version)")
        return

    if not args.description:
        logger.warn(f"{miss_msg} -d (--description)")
        return

    copy_folder(
        src_root=source,
        dst_root=target,
        includes=includes,
        excludes=excludes,
        use_gitignore=True,
        confirm_before_copy=False,
        remove_existing=True,
        confirm_before_remove=False,
    )

    rename_texts(
        root=target,
        renames_dict={
            "pypitemp": args.name,
        },
        includes=includes,
        excludes=excludes,
    )

    rename_texts(
        root=target,
        renames_dict={
            r"version\s*=\s*\".*\"": f'version = "{args.version}"',
            r"description\s*=\s*\".*\"": f'description = "{args.description}"',
        },
        includes=["pyproject.toml"],
        unmatch_bool=False,
    )


if __name__ == "__main__":
    parser = TemplateArgParser()
    args = parser.parse_args()
    main(args)

    # python template.py -s "." -t "~/repos/temp-test" -n "temp-test" -d "This is a test package" -v "0.0.1"
