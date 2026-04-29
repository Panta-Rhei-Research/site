---
{
  "projection_kind": "taulib_declaration",
  "title": "cattau_countable_witness",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/cattau-countable-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7ToposClassifier`.",
  "declaration_id": "TauLib.BookI.Topos.H7ToposClassifier::cattau_countable_witness",
  "declaration_slug": "cattau-countable-witness",
  "kind": "theorem",
  "name": "cattau_countable_witness",
  "module_name": "TauLib.BookI.Topos.H7ToposClassifier",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/",
  "source_line_start": 177,
  "source_line_end": 180,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L177-L180",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H7ToposClassifier",
        "url": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L177-L180",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Topos.H7ToposClassifier](/verify/taulib/docs/book-i-topos-h7-topos-classifier/)
- Source path: [`TauLib/BookI/Topos/H7ToposClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L177-L180)
- Source range: L177-L180
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §3 Thm `cattau-countable` — countability witness**.

    Cat_τ is countable because its object type TauIdx = Nat is
    countable by definition. -/
```

## Source Excerpt

```lean
theorem cattau_countable_witness :
    -- TauIdx is countable (it's Nat)
    Nonempty (TauIdx → Nat) :=
  ⟨id⟩
```
