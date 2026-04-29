---
{
  "projection_kind": "taulib_declaration",
  "title": "sigmaImpl_N_left",
  "permalink": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/sigma-impl-n-left/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.ParaconsistentSoundness`.",
  "declaration_id": "TauLib.BookI.Topos.ParaconsistentSoundness::sigmaImpl_N_left",
  "declaration_slug": "sigma-impl-n-left",
  "kind": "theorem",
  "name": "sigmaImpl_N_left",
  "module_name": "TauLib.BookI.Topos.ParaconsistentSoundness",
  "module_url": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/",
  "source_line_start": 152,
  "source_line_end": 154,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L152-L154",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L152-L154",
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
- Source path: [`TauLib/BookI/Topos/ParaconsistentSoundness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L152-L154)
- Source range: L152-L154
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem sigmaImpl_N_left (q : Truth4) :
    sigmaImpl N q = match q with | T => T | F => N | B => T | N => N := by
  cases q <;> rfl
```
