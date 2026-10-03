# pow-bench

Reproducible hash-rate benchmarks for proof-of-work algorithms, with a focus on
post-quantum candidates (Poseidon2 over the Goldilocks field) and classic
keccak-based mining.

Why: cloud GPU rental pricing and network-hashrate data are scattered.
This repo builds a **public, reproducible dataset** of per-GPU hashrate /
power figures plus the methodology to re-run them — useful for mining-pool
operators, GPU-cloud economists, and researchers evaluating PoW network
security.

## Datasets

- `datasets/gpu-posetidon2-benchmarks.csv` — per-GPU QPoW (Poseidon2) hashrate,
  source: public community benchmarks (hashrate.no, Kryptex), compiled
  Oct 2026. Revenue reference ≈ $6.52/GH/day at QTC ≈ $172.
- `datasets/keccak-cpu-reference.csv` — measured (not estimated) keccak-256
  throughput on real machines, Oct 2026.

## Method

- `scripts/keccak_bench.py` — pure-Python keccak-256 throughput benchmark.
  Verifies digest against the `UNICHRED` on-chain `digestOf` reference
  (exact match, see `datasets/keccak-cpu-reference.csv`).
- `calc/` — rental-vs-mining margin calculator (input: GPU MH/s, rental
  $/h, token price → output: profit/day, break-even price).

## Reproduce

```bash
python3 scripts/keccak_bench.py --seconds 10
```

## Roadmap

- [ ] Native CUDA Poseidon2 harness vs reference CPU implementation
  (needs RTX 4090/5090 hours — see notes)
- [ ] kW/h-aware economics including pool fees and electricity
- [ ] Weekly refresh of community hashrate table

## License

MIT
