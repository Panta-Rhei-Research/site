---
{
  "projection_kind": "taulib_declaration",
  "title": "ym_coupling_3",
  "permalink": "/verify/taulib/docs/book-iii-physics-gap-theorem/ym-coupling-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.GapTheorem`.",
  "declaration_id": "TauLib.BookIII.Physics.GapTheorem::ym_coupling_3",
  "declaration_slug": "ym-coupling-3",
  "kind": "theorem",
  "name": "ym_coupling_3",
  "module_name": "TauLib.BookIII.Physics.GapTheorem",
  "module_url": "/verify/taulib/docs/book-iii-physics-gap-theorem/",
  "source_line_start": 245,
  "source_line_end": 248,
  "registry_ids": [
    "III.D46"
  ],
  "related_registry_items": [
    {
      "id": "III.D46",
      "title": "Strong Defect Functional",
      "url": "/registry/object/III.D46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L245-L248",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.GapTheorem",
        "url": "/verify/taulib/docs/book-iii-physics-gap-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L245-L248",
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

- Module: [TauLib.BookIII.Physics.GapTheorem](/verify/taulib/docs/book-iii-physics-gap-theorem/)
- Source path: [`TauLib/BookIII/Physics/GapTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L245-L248)
- Source range: L245-L248
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D46` — Strong Defect Functional

## Immediate Comment / Docstring

```lean
/-- [III.D46] Structural: YM coupling at depth 3. -/
```

## Source Excerpt

```lean
theorem ym_coupling_3 :
    ym_sector_coupling 3 > 0 := by native_decide

end Tau.BookIII.Physics
```
