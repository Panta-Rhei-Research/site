---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L290",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/eval-l290/",
  "summary_short": "`eval` declaration in `TauLib.BookI.Polarity.PrimePolarityClassifier`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimePolarityClassifier::#eval:290",
  "declaration_slug": "eval-l290",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookI.Polarity.PrimePolarityClassifier",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/",
  "source_line_start": 290,
  "source_line_end": 290,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L290-L290",
  "formal_status": "computed",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L290-L290",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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
- Source path: [`TauLib/BookI/Polarity/PrimePolarityClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L290-L290)
- Source range: L290-L290
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- PART 5: Concrete numerical demonstrations
-- ============================================================

-- The bipolar partition by direct evaluation:
-- p_1 = 2  → X (label 0, by Kronecker convention χ_2(2) = 0)
-- p_2 = 3  → C (label -1, since (2/3) = -1)
-- p_3 = 5  → C (label -1, since (2/5) = -1)
-- p_4 = 7  → B (label +1, since (2/7) = +1)
-- p_5 = 11 → C (label -1, since (2/11) = -1)
-- p_6 = 13 → C (label -1, since (2/13) = -1)
-- p_7 = 17 → B (label +1, since (2/17) = +1)
-- p_8 = 19 → C (label -1, since (2/19) = -1)
-- p_9 = 23 → B (label +1, since (2/23) = +1)
```

## Source Excerpt

```lean
#eval labelInfty 0    -- 0  (p_1 = 2, X)
```
