---
{
  "projection_kind": "taulib_declaration",
  "title": "isDesignated_join_of_right",
  "permalink": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/is-designated-join-of-right/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.ParaconsistentSoundness`.",
  "declaration_id": "TauLib.BookI.Topos.ParaconsistentSoundness::isDesignated_join_of_right",
  "declaration_slug": "is-designated-join-of-right",
  "kind": "theorem",
  "name": "isDesignated_join_of_right",
  "module_name": "TauLib.BookI.Topos.ParaconsistentSoundness",
  "module_url": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/",
  "source_line_start": 218,
  "source_line_end": 220,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L218-L220",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.ParaconsistentSoundness",
        "url": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L218-L220",
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

- Module: [TauLib.BookI.Topos.ParaconsistentSoundness](/verify/taulib/docs/book-i-topos-paraconsistent-soundness/)
- Source path: [`TauLib/BookI/Topos/ParaconsistentSoundness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L218-L220)
- Source range: L218-L220
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Disjunction introduction (right)**: if `b` is designated,
    so is `a ∨ b`. -/
```

## Source Excerpt

```lean
theorem isDesignated_join_of_right (a b : Truth4)
    (h : IsDesignated b) : IsDesignated (Truth4.join a b) := by
  cases a <;> cases b <;> simp_all [IsDesignated, Truth4.join]
```
