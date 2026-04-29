---
{
  "projection_kind": "taulib_declaration",
  "title": "CayleyDist_eq_zero_iff_rhoCount",
  "permalink": "/verify/taulib/docs/book-i-addressability-cayley-metric/cayley-dist-eq-zero-iff-rho-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.CayleyMetric`.",
  "declaration_id": "TauLib.BookI.Addressability.CayleyMetric::CayleyDist_eq_zero_iff_rhoCount",
  "declaration_slug": "cayley-dist-eq-zero-iff-rho-count",
  "kind": "theorem",
  "name": "CayleyDist_eq_zero_iff_rhoCount",
  "module_name": "TauLib.BookI.Addressability.CayleyMetric",
  "module_url": "/verify/taulib/docs/book-i-addressability-cayley-metric/",
  "source_line_start": 95,
  "source_line_end": 98,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/CayleyMetric.lean#L95-L98",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.CayleyMetric",
        "url": "/verify/taulib/docs/book-i-addressability-cayley-metric/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/CayleyMetric.lean#L95-L98",
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

- Module: [TauLib.BookI.Addressability.CayleyMetric](/verify/taulib/docs/book-i-addressability-cayley-metric/)
- Source path: [`TauLib/BookI/Addressability/CayleyMetric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/CayleyMetric.lean#L95-L98)
- Source range: L95-L98
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Identity-of-indiscernibles for the Cayley pseudometric:
    `CayleyDist = 0` ⇔ same ρ-count.  (NFs with same ρ-count but
    different seed maps have distance 0, capturing the pseudometric
    nature; the strictly-metric refinement layers on in 5b.) -/
```

## Source Excerpt

```lean
theorem CayleyDist_eq_zero_iff_rhoCount (nf₁ nf₂ : NormalForm) :
    CayleyDist nf₁ nf₂ = 0 ↔ nf₁.rhoCount = nf₂.rhoCount := by
  unfold CayleyDist
  exact natAbsDiff_eq_zero_iff _ _
```
