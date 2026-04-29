---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_fiber_rho_fixed",
  "permalink": "/verify/taulib/docs/book-i-orbit-closure/omega-fiber-rho-fixed/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Closure`.",
  "declaration_id": "TauLib.BookI.Orbit.Closure::omega_fiber_rho_fixed",
  "declaration_slug": "omega-fiber-rho-fixed",
  "kind": "theorem",
  "name": "omega_fiber_rho_fixed",
  "module_name": "TauLib.BookI.Orbit.Closure",
  "module_url": "/verify/taulib/docs/book-i-orbit-closure/",
  "source_line_start": 89,
  "source_line_end": 91,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Closure.lean#L89-L91",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Closure",
        "url": "/verify/taulib/docs/book-i-orbit-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Closure.lean#L89-L91",
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

- Module: [TauLib.BookI.Orbit.Closure](/verify/taulib/docs/book-i-orbit-closure/)
- Source path: [`TauLib/BookI/Orbit/Closure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Closure.lean#L89-L91)
- Source range: L89-L91
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All objects in the omega fiber are ρ-fixed. -/
```

## Source Excerpt

```lean
theorem omega_fiber_rho_fixed (n : Nat) :
    rho ⟨omega, n⟩ = ⟨omega, n⟩ :=
  K2_omega_fixed n
```
