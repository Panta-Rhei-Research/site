---
{
  "projection_kind": "taulib_declaration",
  "title": "strictly_increasing_nat",
  "permalink": "/verify/taulib/docs/book-iii-mirror-saturation/strictly-increasing-nat/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Mirror.Saturation`.",
  "declaration_id": "TauLib.BookIII.Mirror.Saturation::strictly_increasing_nat",
  "declaration_slug": "strictly-increasing-nat",
  "kind": "theorem",
  "name": "strictly_increasing_nat",
  "module_name": "TauLib.BookIII.Mirror.Saturation",
  "module_url": "/verify/taulib/docs/book-iii-mirror-saturation/",
  "source_line_start": 304,
  "source_line_end": 310,
  "registry_ids": [
    "III.P31"
  ],
  "related_registry_items": [
    {
      "id": "III.P31",
      "title": "Terminal Level Characterization",
      "url": "/registry/object/III.P31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L304-L310",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.Saturation",
        "url": "/verify/taulib/docs/book-iii-mirror-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L304-L310",
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

- Module: [TauLib.BookIII.Mirror.Saturation](/verify/taulib/docs/book-iii-mirror-saturation/)
- Source path: [`TauLib/BookIII/Mirror/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L304-L310)
- Source range: L304-L310
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P31` — Terminal Level Characterization

## Immediate Comment / Docstring

```lean
/-- [III.P31] Structural: the enrichment levels have strictly
    increasing toNat values (witnesses total order). -/
```

## Source Excerpt

```lean
theorem strictly_increasing_nat :
    EnrLevel.E0.toNat < EnrLevel.E1.toNat ∧
    EnrLevel.E1.toNat < EnrLevel.E2.toNat ∧
    EnrLevel.E2.toNat < EnrLevel.E3.toNat := by
  exact ⟨by decide, by decide, by decide⟩

end Tau.BookIII.Mirror
```
