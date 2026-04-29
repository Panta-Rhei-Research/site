---
{
  "projection_kind": "taulib_declaration",
  "title": "no_new_lobe",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/no-new-lobe/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::no_new_lobe",
  "declaration_slug": "no-new-lobe",
  "kind": "theorem",
  "name": "no_new_lobe",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 208,
  "source_line_end": 219,
  "registry_ids": [
    "VII.L05"
  ],
  "related_registry_items": [
    {
      "id": "VII.L05",
      "title": "No-New-Lobe Lemma",
      "url": "/registry/object/VII.L05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L208-L219",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L208-L219",
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
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L208-L219)
- Source range: L208-L219
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.L05` — No-New-Lobe Lemma

## Immediate Comment / Docstring

```lean
/-- [VII.L05] No-New-Lobe: five generators partition into exactly four ρ-orbits.
    No sixth generator constructible; lemniscate topology exhausts topological features.
    |Orb(ρ)| = 4 and Orb(ρ) is closed under ρ. -/
```

## Source Excerpt

```lean
theorem no_new_lobe :
    -- Five generators
    ([Generator.alpha, .pi, .pi_prime, .pi_dprime, .omega].length = 5) ∧
    -- Four orbits
    ([Orbit.identity, .lobes, .crossing, .closure].length = 4) ∧
    -- Orbit assignment covers all generators
    (Generator.alpha.orbit = .identity) ∧
    (Generator.pi.orbit = .lobes) ∧
    (Generator.pi_prime.orbit = .lobes) ∧
    (Generator.pi_dprime.orbit = .crossing) ∧
    (Generator.omega.orbit = .closure) :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
```
