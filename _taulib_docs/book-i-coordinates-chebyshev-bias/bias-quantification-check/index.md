---
{
  "projection_kind": "taulib_declaration",
  "title": "bias_quantification_check",
  "permalink": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/bias-quantification-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.ChebyshevBias`.",
  "declaration_id": "TauLib.BookI.Coordinates.ChebyshevBias::bias_quantification_check",
  "declaration_slug": "bias-quantification-check",
  "kind": "def",
  "name": "bias_quantification_check",
  "module_name": "TauLib.BookI.Coordinates.ChebyshevBias",
  "module_url": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/",
  "source_line_start": 105,
  "source_line_end": 108,
  "registry_ids": [
    "I.D98"
  ],
  "related_registry_items": [
    {
      "id": "I.D98",
      "title": "Galois Group of Primorial Stage",
      "url": "/registry/object/I.D98/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L105-L108",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.ChebyshevBias",
        "url": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L105-L108",
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

- Module: [TauLib.BookI.Coordinates.ChebyshevBias](/verify/taulib/docs/book-i-coordinates-chebyshev-bias/)
- Source path: [`TauLib/BookI/Coordinates/ChebyshevBias.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L105-L108)
- Source range: L105-L108
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D98` — Galois Group of Primorial Stage

## Immediate Comment / Docstring

```lean
/-- [I.D98] Bias quantification: the bias for (q=4, a=3 vs a=1) is
    positive up to x. That is, π(n;4,3) > π(n;4,1) more often than not. -/
```

## Source Excerpt

```lean
def bias_quantification_check (bound : Nat) : Bool :=
  let wins_3 := chebyshev_bias bound 4 3 1  -- times 3 mod 4 leads
  let wins_1 := chebyshev_bias bound 4 1 3  -- times 1 mod 4 leads
  wins_3 > wins_1  -- Chebyshev bias: non-residues typically lead
```
