---
{
  "projection_kind": "taulib_declaration",
  "title": "regime_summary_table",
  "permalink": "/verify/taulib/docs/book-iv-many-body-condensed-matter/regime-summary-table/",
  "summary_short": "`def` declaration in `TauLib.BookIV.ManyBody.CondensedMatter`.",
  "declaration_id": "TauLib.BookIV.ManyBody.CondensedMatter::regime_summary_table",
  "declaration_slug": "regime-summary-table",
  "kind": "def",
  "name": "regime_summary_table",
  "module_name": "TauLib.BookIV.ManyBody.CondensedMatter",
  "module_url": "/verify/taulib/docs/book-iv-many-body-condensed-matter/",
  "source_line_start": 236,
  "source_line_end": 247,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L236-L247",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.CondensedMatter",
        "url": "/verify/taulib/docs/book-iv-many-body-condensed-matter/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L236-L247",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookIV.ManyBody.CondensedMatter](/verify/taulib/docs/book-iv-many-body-condensed-matter/)
- Source path: [`TauLib/BookIV/ManyBody/CondensedMatter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L236-L247)
- Source range: L236-L247
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The complete 10-regime classification. -/
```

## Source Excerpt

```lean
def regime_summary_table : List RegimeSummary := [
  ⟨"Crystal",        "non-topological", "all arrested, periodic"⟩,
  ⟨"Quasicrystal",   "non-topological", "all arrested, irrational winding"⟩,
  ⟨"Glass",          "non-topological", "mu,nu arrested, kappa unfrozen"⟩,
  ⟨"Euler",          "non-topological", "mu <= mu_crit, budget conserved"⟩,
  ⟨"Navier-Stokes",  "non-topological", "mu > mu_crit, dissipative"⟩,
  ⟨"Plasma",         "non-topological", "all above threshold, theta fluctuating"⟩,
  ⟨"MHD",            "non-topological", "nu >> mu, B-sector coupled"⟩,
  ⟨"Superfluid",     "topological",     "maximal mu, quantized theta, no EM"⟩,
  ⟨"Superconductor", "topological",     "maximal mu_B, quantized flux, EM coupled"⟩,
  ⟨"Ferromagnet",    "topological",     "d4 globally aligned, Curie transition"⟩
]
```
