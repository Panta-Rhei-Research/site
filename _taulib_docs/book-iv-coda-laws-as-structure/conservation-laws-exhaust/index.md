---
{
  "projection_kind": "taulib_declaration",
  "title": "conservation_laws_exhaust",
  "permalink": "/corpus/taulib/docs/book-iv-coda-laws-as-structure/conservation-laws-exhaust/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Coda.LawsAsStructure`.",
  "declaration_id": "TauLib.BookIV.Coda.LawsAsStructure::conservation_laws_exhaust",
  "declaration_slug": "conservation-laws-exhaust",
  "kind": "theorem",
  "name": "conservation_laws_exhaust",
  "module_name": "TauLib.BookIV.Coda.LawsAsStructure",
  "module_url": "/corpus/taulib/docs/book-iv-coda-laws-as-structure/",
  "source_line_start": 122,
  "source_line_end": 126,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L122-L126",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.LawsAsStructure",
        "url": "/corpus/taulib/docs/book-iv-coda-laws-as-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L122-L126",
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

- Module: [TauLib.BookIV.Coda.LawsAsStructure](/corpus/taulib/docs/book-iv-coda-laws-as-structure/)
- Source path: [`TauLib/BookIV/Coda/LawsAsStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L122-L126)
- Source range: L122-L126
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All conservation laws are tower-natural. -/
```

## Source Excerpt

```lean
theorem conservation_laws_exhaust (c : ConservationLaw) :
    c = .Energy ∨ c = .Momentum ∨ c = .AngularMomentum ∨
    c = .ElectricCharge ∨ c = .ColorCharge ∨ c = .BaryonNumber ∨
    c = .LeptonNumber ∨ c = .TopologicalCharge := by
  cases c <;> simp
```
