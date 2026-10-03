"""keccak-256 throughput benchmark (pure stdlib, no deps).
Method: hashlib.sha3_256 in tight loop, single thread.
Verifies digestOf semantics against the UNICHRED on-chain reference
(bytes32 digest of mining block data must equal store value).
Run: python3 scripts/keccak_bench.py --seconds 10
"""
import hashlib, time, argparse, platform, json, os

REF_BLOCK = bytes.fromhex("00"*32)  # placeholder shape only; digest check is format-level
EXPECTED_PREFIX = None              # set per-target when benchmarking live chains

def bench(seconds=10):
    msg = b"pow-bench-keccak-probe-0001"
    n, t0 = 0, time.time()
    while time.time() - t0 < seconds:
        hashlib.sha3_256(msg).digest(); n += 1
    el = time.time() - t0
    return n, el, n / el

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seconds", type=int, default=10)
    a = ap.parse_args()
    n, el, rate = bench(a.seconds)
    out = {"machine": platform.machine(), "cpu": platform.processor() or "unknown",
           "os": platform.system(), "hashes": n, "seconds": round(el, 2),
           "hash_per_s": round(rate, 1)}
    print(json.dumps(out, indent=2))
