from os import wait
from pydantic import BaseModel
from urllib.parse import quote_plus


class ExternalGenerationRequest(BaseModel):
    bundle_type: str
    genre: str | None = None
    prompt: str | None = None  # For bundle_type = TEXT2MUSIC only
    duration: int | None = None
    instruments: list[str] | None = None
    genre_blend: str | None = None
    energy: str | None = None
    structure_id: int | None = None
    bpm: int | None = None
    key_root: str | None = None
    key_quality: str | None = None


class ExternalAccountLimitsSchema(BaseModel):
    reset_data: dict
    usage_data: dict


class ExternalAuthorizeRequestSchema(BaseModel):
    client_id: str
    grant_type: str
    password: str | None = None
    refresh_token: str | None = None

    def to_params(self) -> str:
        return quote_plus("&".join(f"{k}={v}" for k, v in self.model_dump(exclude_none=True).items()))


class ExternalAuthorizeResponseSchema(BaseModel):
    token_type: str
    expires_in: int
    access_token: str
    refresh_token: str


class _Formula(BaseModel):
    bpm: int | None = None
    key: str | None = None
    genre: str
    energy: str | None = None
    prompt: str | None = None
    entropy: str | None = None
    duration: int | None = None
    user_audio: str | None = None
    genre_blend: str | None = None
    instruments: list[str] | None = None
    extra_params: str | None = None
    structure_id: int | None = None
    prompt: str | None = None


class _VegaSong(BaseModel):
    id: str
    title: str
    duration: int
    music_file_path: str
    wav_file_path: str
    created_at: str
    is_in_library: bool
    xml_file_path: str
    formula: _Formula
    is_preview: bool


class ExternalGenerationSchema(BaseModel):
    id: str
    created_at: str
    formula: _Formula
    type: str
    capacity: int
    is_finished: bool
    vega_songs: list[_VegaSong]
    is_preview: bool
    errors: list
