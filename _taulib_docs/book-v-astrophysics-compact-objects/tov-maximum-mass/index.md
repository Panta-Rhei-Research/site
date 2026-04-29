---
{
  "projection_kind": "taulib_declaration",
  "title": "tov_maximum_mass",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-compact-objects/tov-maximum-mass/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.CompactObjects`.",
  "declaration_id": "TauLib.BookV.Astrophysics.CompactObjects::tov_maximum_mass",
  "declaration_slug": "tov-maximum-mass",
  "kind": "theorem",
  "name": "tov_maximum_mass",
  "module_name": "TauLib.BookV.Astrophysics.CompactObjects",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/",
  "source_line_start": 144,
  "source_line_end": 145,
  "registry_ids": [
    "V.T87"
  ],
  "related_registry_items": [
    {
      "id": "V.T87",
      "title": "TOV Mass Limit --- V.T39",
      "url": "/registry/object/V.T87/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L144-L145",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.CompactObjects",
        "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L144-L145",
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

- Module: [TauLib.BookV.Astrophysics.CompactObjects](/verify/taulib/docs/book-v-astrophysics-compact-objects/)
- Source path: [`TauLib/BookV/Astrophysics/CompactObjects.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L144-L145)
- Source range: L144-L145
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T87` — TOV Mass Limit --- V.T39

## Immediate Comment / Docstring

```lean
/-- [V.T87] TOV maximum mass: neutron stars have a maximum mass
    M_TOV ≈ 2.1-2.5 M_☉ above which the S² topology is
    unsustainable and the coherence horizon crossing occurs.

    The exact value depends on the nuclear EOS, which the
    τ-framework constrains but does not uniquely determine
    from first principles alone. -/
```

## Source Excerpt

```lean
theorem tov_maximum_mass :
    tov_mass_lower < tov_mass_upper := by native_decide
```
