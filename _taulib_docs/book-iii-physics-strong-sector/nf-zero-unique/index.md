---
{
  "projection_kind": "taulib_declaration",
  "title": "nf_zero_unique",
  "permalink": "/verify/taulib/docs/book-iii-physics-strong-sector/nf-zero-unique/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.StrongSector`.",
  "declaration_id": "TauLib.BookIII.Physics.StrongSector::nf_zero_unique",
  "declaration_slug": "nf-zero-unique",
  "kind": "theorem",
  "name": "nf_zero_unique",
  "module_name": "TauLib.BookIII.Physics.StrongSector",
  "module_url": "/verify/taulib/docs/book-iii-physics-strong-sector/",
  "source_line_start": 228,
  "source_line_end": 231,
  "registry_ids": [
    "III.P16"
  ],
  "related_registry_items": [
    {
      "id": "III.P16",
      "title": "NF Discreteness Lemma",
      "url": "/registry/object/III.P16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L228-L231",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.StrongSector",
        "url": "/verify/taulib/docs/book-iii-physics-strong-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L228-L231",
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

- Module: [TauLib.BookIII.Physics.StrongSector](/verify/taulib/docs/book-iii-physics-strong-sector/)
- Source path: [`TauLib/BookIII/Physics/StrongSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L228-L231)
- Source range: L228-L231
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P16` — NF Discreteness Lemma

## Immediate Comment / Docstring

```lean
/-- [III.P16] Structural: BNF of 0 is unique at depth 3. -/
```

## Source Excerpt

```lean
theorem nf_zero_unique :
    boundary_normal_form 0 3 = ⟨0, 0, 0, 3⟩ := by native_decide

end Tau.BookIII.Physics
```
