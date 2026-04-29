---
{
  "projection_kind": "taulib_declaration",
  "title": "w_mass_from_coherence",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/w-mass-from-coherence/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy::w_mass_from_coherence",
  "declaration_slug": "w-mass-from-coherence",
  "kind": "theorem",
  "name": "w_mass_from_coherence",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/",
  "source_line_start": 243,
  "source_line_end": 244,
  "registry_ids": [
    "IV.T54"
  ],
  "related_registry_items": [
    {
      "id": "IV.T54",
      "title": "W Mass from Coherence Fixing",
      "url": "/registry/object/IV.T54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L243-L244",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L243-L244",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy](/verify/taulib/docs/book-iv-electroweak-weak-holonomy/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L243-L244)
- Source range: L243-L244
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T54` — W Mass from Coherence Fixing

## Immediate Comment / Docstring

```lean
/-- [IV.T54] W mass from coherence-fixing scale: the omega-crossing
    singularity fixes a coherence scale Lambda_EW. The W mass is
    M_W = g_wk * Lambda_EW / 2, where g_wk is the weak coupling.
    Structural: the mass is nonzero because Lambda_EW > 0. -/
```

## Source Excerpt

```lean
theorem w_mass_from_coherence :
    w_mass_mev.mass_numer > 0 := by native_decide
```
