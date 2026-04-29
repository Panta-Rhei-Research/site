---
{
  "projection_kind": "taulib_declaration",
  "title": "legendreBClass",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/legendre-bclass/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.PrimePolarityClassifier`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimePolarityClassifier::legendreBClass",
  "declaration_slug": "legendre-bclass",
  "kind": "def",
  "name": "legendreBClass",
  "module_name": "TauLib.BookI.Polarity.PrimePolarityClassifier",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/",
  "source_line_start": 343,
  "source_line_end": 343,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L343-L343",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PrimePolarityClassifier",
        "url": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L343-L343",
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

- Module: [TauLib.BookI.Polarity.PrimePolarityClassifier](/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/)
- Source path: [`TauLib/BookI/Polarity/PrimePolarityClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L343-L343)
- Source range: L343-L343
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Bridge to Wave 17's `chi`**: the bipolar classifier `Label_n`
    instantiates Wave 17's abstract `B_class` predicate via the
    Legendre criterion `Legendre(2/p) = +1`.

    Concretely, take `B_class p := (chi_p p 2 == 1)`.  Then for
    every prime `p ≥ 3`:

      `chi B_class p =`
        `+1` if `Legendre(2/p) = +1` (B-class), or
        `-1` if `Legendre(2/p) = -1` (C-class), or
        `0` if `p = 2` (ramified).

    This gives `Label_n` ↔ Wave 17's `chi` at every prime, closing
    the H2-to-H3 conceptual loop. -/
```

## Source Excerpt

```lean
def legendreBClass : Nat → Bool := fun p => decide (chi_p p 2 = 1)
```
