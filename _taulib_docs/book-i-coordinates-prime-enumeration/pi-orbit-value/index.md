---
{
  "projection_kind": "taulib_declaration",
  "title": "pi_orbit_value",
  "permalink": "/verify/taulib/docs/book-i-coordinates-prime-enumeration/pi-orbit-value/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.PrimeEnumeration`.",
  "declaration_id": "TauLib.BookI.Coordinates.PrimeEnumeration::pi_orbit_value",
  "declaration_slug": "pi-orbit-value",
  "kind": "def",
  "name": "pi_orbit_value",
  "module_name": "TauLib.BookI.Coordinates.PrimeEnumeration",
  "module_url": "/verify/taulib/docs/book-i-coordinates-prime-enumeration/",
  "source_line_start": 96,
  "source_line_end": 96,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L96-L96",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.PrimeEnumeration",
        "url": "/verify/taulib/docs/book-i-coordinates-prime-enumeration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L96-L96",
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

- Module: [TauLib.BookI.Coordinates.PrimeEnumeration](/verify/taulib/docs/book-i-coordinates-prime-enumeration/)
- Source path: [`TauLib/BookI/Coordinates/PrimeEnumeration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L96-L96)
- Source range: L96-L96
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The semantic projection from π-orbit depth to α-orbit value:
    the depth-k element of O_π represents the number nthPrime(k).

    This is the key distinction between structural rank transfer
    (RT_π maps k ↦ ⟨π, k⟩, preserving depth) and semantic projection
    (pi_orbit_value maps k ↦ p_k, giving the denotational value). -/
```

## Source Excerpt

```lean
def pi_orbit_value (k : TauIdx) : TauIdx := nthPrime k
```
