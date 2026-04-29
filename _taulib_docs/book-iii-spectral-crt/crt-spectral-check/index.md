---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_spectral_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-crt/crt-spectral-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.CRT`.",
  "declaration_id": "TauLib.BookIII.Spectral.CRT::crt_spectral_check",
  "declaration_slug": "crt-spectral-check",
  "kind": "def",
  "name": "crt_spectral_check",
  "module_name": "TauLib.BookIII.Spectral.CRT",
  "module_url": "/verify/taulib/docs/book-iii-spectral-crt/",
  "source_line_start": 41,
  "source_line_end": 59,
  "registry_ids": [
    "III.T10"
  ],
  "related_registry_items": [
    {
      "id": "III.T10",
      "title": "CRT Decomposition Theorem",
      "url": "/registry/object/III.T10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L41-L59",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L41-L59",
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
- Source path: [`TauLib/BookIII/Spectral/CRT.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L41-L59)
- Source range: L41-L59
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T10` — CRT Decomposition Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T10] CRT spectral decomposition at enriched level.
    Verifies that crt_decompose ∘ crt_reconstruct = id at each
    primorial level, enriched by tower coherence. -/
```

## Source Excerpt

```lean
def crt_spectral_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- CRT round-trip at depth k
      let residues := crt_decompose x k
      let reconstructed := crt_reconstruct residues k
      let roundtrip_ok := reconstructed == reduce x k
      -- Tower coherence: CRT at k+1 projects to CRT at k
      let high_residues := crt_decompose x (k + 1)
      let high_reconstructed := crt_reconstruct high_residues (k + 1)
      let projected := reduce high_reconstructed k
      let tower_ok := projected == reduce x k
      roundtrip_ok && tower_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
