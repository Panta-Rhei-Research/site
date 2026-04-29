---
{
  "projection_kind": "taulib_declaration",
  "title": "polarity_difference",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/polarity-difference/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.WeakChirality2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality2::polarity_difference",
  "declaration_slug": "polarity-difference",
  "kind": "def",
  "name": "polarity_difference",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/",
  "source_line_start": 190,
  "source_line_end": 191,
  "registry_ids": [
    "IV.P174"
  ],
  "related_registry_items": [
    {
      "id": "IV.P174",
      "title": "Polarity-switching requires balanced polarity",
      "url": "/registry/object/IV.P174/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L190-L191",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakChirality2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L190-L191",
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality2](/verify/taulib/docs/book-iv-electroweak-weak-chirality2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality2.lean#L190-L191)
- Source range: L190-L191
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.P174` — Polarity-switching requires balanced polarity

## Immediate Comment / Docstring

```lean
/-- [IV.P174] Polarity-switching transitions are suppressed in sectors
    with unbalanced polarity. The suppression factor is exp(-|pol(X)|)
    where pol(X) = chi_plus - chi_minus. For unbalanced sectors,
    |pol| > 0, so transitions are exponentially suppressed.
    For the balanced A-sector, |pol| = 0 and there is no suppression.

    Structural: we verify that only A has pol = 0. -/
```

## Source Excerpt

```lean
def polarity_difference (p : PolarityIndex) : Int :=
  (Int.ofNat p.chi_plus) - (Int.ofNat p.chi_minus)
```
