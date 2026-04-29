---
{
  "projection_kind": "taulib_declaration",
  "title": "reconstruction_tower_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-crt/reconstruction-tower-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.CRT`.",
  "declaration_id": "TauLib.BookIII.Spectral.CRT::reconstruction_tower_check",
  "declaration_slug": "reconstruction-tower-check",
  "kind": "def",
  "name": "reconstruction_tower_check",
  "module_name": "TauLib.BookIII.Spectral.CRT",
  "module_url": "/verify/taulib/docs/book-iii-spectral-crt/",
  "source_line_start": 148,
  "source_line_end": 161,
  "registry_ids": [
    "III.D20"
  ],
  "related_registry_items": [
    {
      "id": "III.D20",
      "title": "Reconstruction Functor",
      "url": "/registry/object/III.D20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L148-L161",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.CRT",
        "url": "/verify/taulib/docs/book-iii-spectral-crt/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L148-L161",
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

- Module: [TauLib.BookIII.Spectral.CRT](/verify/taulib/docs/book-iii-spectral-crt/)
- Source path: [`TauLib/BookIII/Spectral/CRT.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L148-L161)
- Source range: L148-L161
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D20` — Reconstruction Functor

## Immediate Comment / Docstring

```lean
/-- [III.D20] Reconstruction functor respects tower: R_{k+1} projects
    to R_k under reduce. -/
```

## Source Excerpt

```lean
def reconstruction_tower_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      let residues_high := crt_decompose (reduce x (k + 1)) (k + 1)
      let reconstructed_high := crt_reconstruct residues_high (k + 1)
      let projected := reduce reconstructed_high k
      let reconstructed_low := reduce x k
      projected == reconstructed_low && go x (k + 1) (fuel - 1)
  termination_by fuel
```
