---
{
  "projection_kind": "taulib_declaration",
  "title": "pi_projection_via_RT",
  "permalink": "/corpus/taulib/docs/book-i-coordinates-prime-enumeration/pi-projection-via-rt/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.PrimeEnumeration`.",
  "declaration_id": "TauLib.BookI.Coordinates.PrimeEnumeration::pi_projection_via_RT",
  "declaration_slug": "pi-projection-via-rt",
  "kind": "theorem",
  "name": "pi_projection_via_RT",
  "module_name": "TauLib.BookI.Coordinates.PrimeEnumeration",
  "module_url": "/corpus/taulib/docs/book-i-coordinates-prime-enumeration/",
  "source_line_start": 100,
  "source_line_end": 102,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L100-L102",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.PrimeEnumeration",
        "url": "/corpus/taulib/docs/book-i-coordinates-prime-enumeration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L100-L102",
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

- Module: [TauLib.BookI.Coordinates.PrimeEnumeration](/corpus/taulib/docs/book-i-coordinates-prime-enumeration/)
- Source path: [`TauLib/BookI/Coordinates/PrimeEnumeration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L100-L102)
- Source range: L100-L102
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The π-orbit projection via rank transfer:
    RT_α(nthPrime(k)) is the α-orbit element corresponding to π_k. -/
```

## Source Excerpt

```lean
theorem pi_projection_via_RT (k : TauIdx) :
    RT alpha (pi_orbit_value k) = toAlphaOrbit (nthPrime k) := by
  simp [pi_orbit_value, RT_alpha_eq]
```
