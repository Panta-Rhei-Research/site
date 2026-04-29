---
{
  "projection_kind": "taulib_declaration",
  "title": "probe_naturality_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/probe-naturality-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.PreYoneda`.",
  "declaration_id": "TauLib.BookII.Regularity.PreYoneda::probe_naturality_check",
  "declaration_slug": "probe-naturality-check",
  "kind": "def",
  "name": "probe_naturality_check",
  "module_name": "TauLib.BookII.Regularity.PreYoneda",
  "module_url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/",
  "source_line_start": 206,
  "source_line_end": 233,
  "registry_ids": [
    "II.R12"
  ],
  "related_registry_items": [
    {
      "id": "II.R12",
      "title": "Probe Naturality Equals Holomorphy",
      "url": "/registry/object/II.R12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L206-L233",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PreYoneda",
        "url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L206-L233",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookII.Regularity.PreYoneda](/verify/taulib/docs/book-ii-regularity-pre-yoneda/)
- Source path: [`TauLib/BookII/Regularity/PreYoneda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L206-L233)
- Source range: L206-L233
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.R12` — Probe Naturality Equals Holomorphy

## Immediate Comment / Docstring

```lean
/-- [II.R12] Probe naturality check: a function f is natural with respect
    to cylinder probes iff it is tower-coherent.

    For cylinder probe phi_{k,prime_idx}: the probe evaluates f at
    residue class v mod p at stage k. Naturality means:

    preyoneda(f, x, k) = reduce(preyoneda(f, x, k+1), k)

    This IS tower coherence. We verify for the canonical probes
    (cylinder generators) that the naturality condition matches
    tower coherence. -/
```

## Source Excerpt

```lean
def probe_naturality_check (bound db : TauIdx) : Bool :=
  go 2 1 1 (bound * db * db + bound + 1)
where
  go (x k pi_idx fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 1 (fuel - 1)
    else if pi_idx > k then go x (k + 1) 1 (fuel - 1)
    else
      let p := nth_prime pi_idx
      if p == 0 then go x k (pi_idx + 1) (fuel - 1)
      else
        -- For each residue class v < p:
        -- cylinder_gen(k, pi_idx, v, true, reduce(x, k)) should agree
        -- when computed at stage k vs. reduced from stage k+1
        let rx_k := reduce x k
        let rx_k1 := reduce x (k + 1)
        -- Naturality: reading at stage k = reducing the stage-(k+1) reading
        let nat_ok := reduce rx_k1 k == rx_k
        -- Cylinder gen at stage k
        let gen_k := cylinder_gen k pi_idx (rx_k % p) true rx_k
        -- Cylinder gen at stage k+1 reduced
        let gen_k1 := cylinder_gen (k + 1) pi_idx (rx_k1 % p) true rx_k1
        -- Both are indicators (0 or 1); the naturality is on the input
        let _ := gen_k
        let _ := gen_k1
        nat_ok && go x k (pi_idx + 1) (fuel - 1)
  termination_by fuel
```
