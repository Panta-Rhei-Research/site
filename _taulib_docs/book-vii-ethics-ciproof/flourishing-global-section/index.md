---
{
  "projection_kind": "taulib_declaration",
  "title": "flourishing_global_section",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/flourishing-global-section/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::flourishing_global_section",
  "declaration_slug": "flourishing-global-section",
  "kind": "theorem",
  "name": "flourishing_global_section",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 307,
  "source_line_end": 310,
  "registry_ids": [
    "VII.T34"
  ],
  "related_registry_items": [
    {
      "id": "VII.T34",
      "title": "Flourishing as Global Section",
      "url": "/registry/object/VII.T34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L307-L310",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L307-L310",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L307-L310)
- Source range: L307-L310
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T34` — Flourishing as Global Section

## Immediate Comment / Docstring

```lean
/-- [VII.T34] Flourishing as Global Section (ch86).
    V = virtue sheaf over life-stages L.
    Flourishing = Γ(L, V). Exists iff:
    (1) Local virtue at each life-stage (fixed-point locally)
    (2) Gluing across life-stages (agreement on overlaps)
    (3) Global existence (sheaf condition over life-course) -/
```

## Source Excerpt

```lean
theorem flourishing_global_section :
    character.has_habituation = true ∧
    character.virtue_is_fixed = true :=
  ⟨rfl, rfl⟩
```
