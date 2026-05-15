---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_ladder_8",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-primorial-ladder/primorial-ladder-8/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.PrimorialLadder`.",
  "declaration_id": "TauLib.BookIII.Spectral.PrimorialLadder::primorial_ladder_8",
  "declaration_slug": "primorial-ladder-8",
  "kind": "theorem",
  "name": "primorial_ladder_8",
  "module_name": "TauLib.BookIII.Spectral.PrimorialLadder",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-primorial-ladder/",
  "source_line_start": 154,
  "source_line_end": 155,
  "registry_ids": [
    "III.D19"
  ],
  "related_registry_items": [
    {
      "id": "III.D19",
      "title": "Primorial Ladder",
      "url": "/registry/object/III.D19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L154-L155",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.PrimorialLadder",
        "url": "/corpus/taulib/docs/book-iii-spectral-primorial-ladder/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L154-L155",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIII.Spectral.PrimorialLadder](/corpus/taulib/docs/book-iii-spectral-primorial-ladder/)
- Source path: [`TauLib/BookIII/Spectral/PrimorialLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L154-L155)
- Source range: L154-L155
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D19` — Primorial Ladder

## Immediate Comment / Docstring

```lean
-- ============================================================
-- FORMAL VERIFICATION (native_decide)
-- ============================================================

-- Primorial ladder [III.D19]
```

## Source Excerpt

```lean
theorem primorial_ladder_8 :
    primorial_ladder_check 8 = true := by native_decide
```
