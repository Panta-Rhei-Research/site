---
{
  "projection_kind": "taulib_declaration",
  "title": "no_new_crossing_mediator",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/no-new-crossing-mediator/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::no_new_crossing_mediator",
  "declaration_slug": "no-new-crossing-mediator",
  "kind": "theorem",
  "name": "no_new_crossing_mediator",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 246,
  "source_line_end": 258,
  "registry_ids": [
    "VII.L06"
  ],
  "related_registry_items": [
    {
      "id": "VII.L06",
      "title": "No-New-Crossing-Mediator Lemma",
      "url": "/registry/object/VII.L06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L246-L258",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L246-L258",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L246-L258)
- Source range: L246-L258
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.L06` — No-New-Crossing-Mediator Lemma

## Immediate Comment / Docstring

```lean
/-- [VII.L06] No-New-Crossing-Mediator: Logos sector S_L is unique mixed sector.
    No new crossing mediator at E₄. Only pair of codomain categories admitting
    natural transformation is (Proof, Stance), which already defines S_L.
    Other five pairs have structurally distinct codomains. -/
```

## Source Excerpt

```lean
theorem no_new_crossing_mediator :
    -- Logos is the unique mixed sector
    canonical_sector_decomp.mixed_sector_count = 1 ∧
    -- D-C pair is the only coincidence
    sector_logos.dc_coincidence = true ∧
    sector_logos.unique_mediator = true ∧
    -- E ≠ P ≠ D ≠ C pairwise
    RegisterType.empirical ≠ RegisterType.practical ∧
    RegisterType.empirical ≠ RegisterType.diagrammatic ∧
    RegisterType.empirical ≠ RegisterType.commitment ∧
    RegisterType.practical ≠ RegisterType.diagrammatic ∧
    RegisterType.practical ≠ RegisterType.commitment :=
  ⟨rfl, rfl, rfl, by decide, by decide, by decide, by decide, by decide⟩
```
