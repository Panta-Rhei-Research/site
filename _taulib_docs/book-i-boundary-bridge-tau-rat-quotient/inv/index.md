---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.inv",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/inv/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Bridge.TauRatQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRatQuotient::TauRat.inv",
  "declaration_slug": "inv",
  "kind": "def",
  "name": "TauRat.inv",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/",
  "source_line_start": 174,
  "source_line_end": 183,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L174-L183",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L174-L183",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRatQuotient](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L174-L183)
- Source range: L174-L183
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- TauRat-level multiplicative inverse. For nonzero `q : TauRat`,
    swaps numerator and denominator with sign adjustment. For zero,
    returns zero (Mathlib's standard convention `inv 0 = 0`). -/
```

## Source Excerpt

```lean
def TauRat.inv (q : TauRat) : TauRat :=
  if hgt : q.num.pos > q.num.neg then
    -- q.num.toInt > 0, so q > 0; inv = ⟨⟨den, 0⟩, pos-neg, _⟩
    ⟨⟨q.den, 0⟩, q.num.pos - q.num.neg, Nat.sub_pos_of_lt hgt⟩
  else if hlt : q.num.neg > q.num.pos then
    -- q.num.toInt < 0, so q < 0; inv = ⟨⟨0, den⟩, neg-pos, _⟩
    ⟨⟨0, q.den⟩, q.num.neg - q.num.pos, Nat.sub_pos_of_lt hlt⟩
  else
    -- pos = neg, so q.toInt = 0 → q ≈ 0; return 0 (Mathlib convention)
    TauRat.zero
```
