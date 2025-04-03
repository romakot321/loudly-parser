from enum import Enum
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field

from app.schemas import BaseSearchSchema


class TaskSchema(BaseModel):
    class TaskItem(BaseModel):
        id: int
        title: str
        music_url: str

        model_config = ConfigDict(from_attributes=True)

    id: UUID
    error: str | None = None
    items: list[TaskItem]

    model_config = ConfigDict(from_attributes=True)


class TaskGenre(Enum):
    ambient = 'Ambient'
    drumnbass = "Drum 'n' Bass"
    edm = "EDM"
    epic_score = "Epic Score"
    hiphop = "Hip Hop"
    house = "House"
    lofi = "Lo Fi"
    reggaeton = "Reggaeton"
    synthwave = "Synthwave"
    techno = "Techno"
    trap_double_tempo = "Trap Double Tempo"
    trap_half_tempo = "Trap Half Tempo"
    downtempo = "Downtempo"
    rock = "Rock"
    zen = "Zen"


class TaskInstument(Enum):
    drums = "DRUMS"
    synth = "SYNTH"
    fx = "FX"
    bass = "BASS"
    percussion = "PERCUSSION"
    keys = "KEYS"
    vocals = "VOCALS"


class TaskEnergy(Enum):
    low = 'low'
    original = 'original'
    high = 'high'


class TaskKeyQuality(Enum):
    minor = 'minor'
    major = 'major'


class TaskKeyRoot(Enum):
    a = 'A'
    b = 'B'
    c = 'C'
    d = 'D'
    e = 'E'
    f = 'F'
    g = 'G'


class TaskStructureId(Enum):
    classic = 0
    to_the_bone = 1
    wait_for_it = 2
    slow_burn = 3


class TaskCreateAdvancedSchema(BaseModel):
    user_id: UUID
    app_bundle: str

    genre: TaskGenre
    duration: int | None = None
    instruments: list[TaskInstument] | None = Field(max_length=7, default=None)
    genre_blend: TaskGenre | None = None
    energy: TaskEnergy | None = None
    structure_id: TaskStructureId | None = None
    bpm: int | None = None
    key_root: TaskKeyRoot | None = None
    key_quality: TaskKeyQuality | None = None


class TaskCreateTextSchema(BaseModel):
    user_id: UUID
    app_bundle: str

    prompt: str
