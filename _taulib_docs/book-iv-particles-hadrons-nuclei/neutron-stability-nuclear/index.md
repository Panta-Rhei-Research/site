---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutronStabilityNuclear",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/neutron-stability-nuclear/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::NeutronStabilityNuclear",
  "declaration_slug": "neutron-stability-nuclear",
  "kind": "structure",
  "name": "NeutronStabilityNuclear",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 356,
  "source_line_end": 363,
  "registry_ids": [
    "IV.R138"
  ],
  "related_registry_items": [
    {
      "id": "IV.R138",
      "title": "Neutron stability inside nuclei",
      "url": "/registry/object/IV.R138/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L356-L363",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.HadronsNuclei",
        "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L356-L363",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Particles.HadronsNuclei](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/)
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L356-L363)
- Source range: L356-L363
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R138` — Neutron stability inside nuclei

## Immediate Comment / Docstring

```lean
/-- [IV.R138] Free neutrons decay in ~10 min, but bound neutrons are stable
    because nuclear binding makes Q_β < 0 (energetically forbidden).
    This is a readout-level phenomenon; the ontic neutron is unchanged. -/
```

## Source Excerpt

```lean
structure NeutronStabilityNuclear where
  /-- Free lifetime (minutes, approx). -/
  free_lifetime_min : Nat := 10
  /-- Stable in nuclei. -/
  stable_in_nuclei : Bool := true
  /-- Mechanism: Q_β < 0. -/
  mechanism : String := "nuclear binding makes Q_beta < 0"
  deriving Repr
```
