---
{
  "projection_kind": "taulib_declaration",
  "title": "bias_mod3_check",
  "permalink": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/bias-mod3-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.ChebyshevBias`.",
  "declaration_id": "TauLib.BookI.Coordinates.ChebyshevBias::bias_mod3_check",
  "declaration_slug": "bias-mod3-check",
  "kind": "def",
  "name": "bias_mod3_check",
  "module_name": "TauLib.BookI.Coordinates.ChebyshevBias",
  "module_url": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/",
  "source_line_start": 111,
  "source_line_end": 114,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L111-L114",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L111-L114",
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
- Source path: [`TauLib/BookI/Coordinates/ChebyshevBias.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L111-L114)
- Source range: L111-L114
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D98` — Galois Group of Primorial Stage

## Immediate Comment / Docstring

```lean
/-- [I.D98] Bias for q=3: π(x;3,2) vs π(x;3,1). -/
```

## Source Excerpt

```lean
def bias_mod3_check (bound : Nat) : Bool :=
  let wins_2 := chebyshev_bias bound 3 2 1
  let wins_1 := chebyshev_bias bound 3 1 2
  wins_2 >= wins_1  -- 2 mod 3 typically leads
```
