---
{
  "projection_kind": "taulib_declaration",
  "title": "max_principle_asymmetry",
  "permalink": "/corpus/taulib/docs/book-ii-mirror-wave-holomorphy/max-principle-asymmetry/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.WaveHolomorphy`.",
  "declaration_id": "TauLib.BookII.Mirror.WaveHolomorphy::max_principle_asymmetry",
  "declaration_slug": "max-principle-asymmetry",
  "kind": "theorem",
  "name": "max_principle_asymmetry",
  "module_name": "TauLib.BookII.Mirror.WaveHolomorphy",
  "module_url": "/corpus/taulib/docs/book-ii-mirror-wave-holomorphy/",
  "source_line_start": 110,
  "source_line_end": 113,
  "registry_ids": [
    "II.T44"
  ],
  "related_registry_items": [
    {
      "id": "II.T44",
      "title": "Asymmetric Determination",
      "url": "/registry/object/II.T44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L110-L113",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.WaveHolomorphy",
        "url": "/corpus/taulib/docs/book-ii-mirror-wave-holomorphy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L110-L113",
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

- Module: [TauLib.BookII.Mirror.WaveHolomorphy](/corpus/taulib/docs/book-ii-mirror-wave-holomorphy/)
- Source path: [`TauLib/BookII/Mirror/WaveHolomorphy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L110-L113)
- Source range: L110-L113
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.T44` — Asymmetric Determination

## Immediate Comment / Docstring

```lean
/-- [II.T44] The elliptic classification has the maximum principle;
    the hyperbolic does not. -/
```

## Source Excerpt

```lean
theorem max_principle_asymmetry :
    elliptic_classification.has_max_principle = true ∧
    hyperbolic_classification.has_max_principle = false := by
  exact ⟨rfl, rfl⟩
```
