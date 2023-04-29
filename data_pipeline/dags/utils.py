from pathlib import Path
import pendulum
from airflow.models import Variable
from docker.types import Mount


class AppConst:
    DOCKER_USER = Variable.get("DOCKER_USER", "ptson")


class AppPath:
    MLOPS_CRASH_COURSE_CODE_DIR = Path(Variable.get("MLOPS_CRASH_COURSE_CODE_DIR"))
    DATA_PIPELINE_DIR = MLOPS_CRASH_COURSE_CODE_DIR / "data_pipeline"
    FEATURE_REPO = DATA_PIPELINE_DIR / "feature_repo"


class DefaultConfig:
    DEFAULT_DAG_ARGS = {
        "owner": "ptson",
        "retries": 0,
        "retry_delay": pendulum.duration(seconds=20),
    }

    DEFAULT_DOCKER_OPERATOR_ARGS = {
        "image": f"{AppConst.DOCKER_USER}/mlops_crash_course/data_pipeline:latest",
        "api_version": "auto",
        "auto_remove": True,
        "mounts": [
            # feature repo
            Mount(
                source=AppPath.FEATURE_REPO.absolute().as_posix(),
                target="/data_pipeline/feature_repo",
                type="bind",
            ),
        ],
    }