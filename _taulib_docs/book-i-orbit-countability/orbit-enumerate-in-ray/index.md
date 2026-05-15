---
{
  "projection_kind": "taulib_declaration",
  "title": "orbit_enumerate_in_ray",
  "permalink": "/corpus/taulib/docs/book-i-orbit-countability/orbit-enumerate-in-ray/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Countability`.",
  "declaration_id": "TauLib.BookI.Orbit.Countability::orbit_enumerate_in_ray",
  "declaration_slug": "orbit-enumerate-in-ray",
  "kind": "theorem",
  "name": "orbit_enumerate_in_ray",
  "module_name": "TauLib.BookI.Orbit.Countability",
  "module_url": "/corpus/taulib/docs/book-i-orbit-countability/",
  "source_line_start": 46,
  "source_line_end": 48,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L46-L48",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Countability",
        "url": "/corpus/taulib/docs/book-i-orbit-countability/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L46-L48",
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

- Module: [TauLib.BookI.Orbit.Countability](/corpus/taulib/docs/book-i-orbit-countability/)
- Source path: [`TauLib/BookI/Orbit/Countability.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L46-L48)
- Source range: L46-L48
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Orbit enumeration produces elements in the orbit ray. -/
```

## Source Excerpt

```lean
theorem orbit_enumerate_in_ray (g : Generator) (hg : g ≠ omega) (n : Nat) :
    OrbitRay g (orbitEnumerate g hg n) := by
  exact ⟨rfl, hg⟩
```
