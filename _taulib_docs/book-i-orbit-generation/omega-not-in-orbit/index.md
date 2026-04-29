---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_not_in_orbit",
  "permalink": "/verify/taulib/docs/book-i-orbit-generation/omega-not-in-orbit/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Generation`.",
  "declaration_id": "TauLib.BookI.Orbit.Generation::omega_not_in_orbit",
  "declaration_slug": "omega-not-in-orbit",
  "kind": "theorem",
  "name": "omega_not_in_orbit",
  "module_name": "TauLib.BookI.Orbit.Generation",
  "module_url": "/verify/taulib/docs/book-i-orbit-generation/",
  "source_line_start": 125,
  "source_line_end": 129,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L125-L129",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Generation",
        "url": "/verify/taulib/docs/book-i-orbit-generation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L125-L129",
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

- Module: [TauLib.BookI.Orbit.Generation](/verify/taulib/docs/book-i-orbit-generation/)
- Source path: [`TauLib/BookI/Orbit/Generation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L125-L129)
- Source range: L125-L129
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Omega is not in any orbit ray. -/
```

## Source Excerpt

```lean
theorem omega_not_in_orbit (g : Generator) (hg : g ≠ omega) (n : Nat) :
    ¬ OrbitRay g ⟨omega, n⟩ := by
  intro ⟨hseed, _⟩
  simp at hseed
  exact hg hseed.symm
```
