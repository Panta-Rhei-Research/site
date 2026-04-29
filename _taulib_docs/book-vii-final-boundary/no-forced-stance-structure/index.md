---
{
  "projection_kind": "taulib_declaration",
  "title": "NoForcedStanceStructure",
  "permalink": "/verify/taulib/docs/book-vii-final-boundary/no-forced-stance-structure/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Final.Boundary`.",
  "declaration_id": "TauLib.BookVII.Final.Boundary::NoForcedStanceStructure",
  "declaration_slug": "no-forced-stance-structure",
  "kind": "structure",
  "name": "NoForcedStanceStructure",
  "module_name": "TauLib.BookVII.Final.Boundary",
  "module_url": "/verify/taulib/docs/book-vii-final-boundary/",
  "source_line_start": 185,
  "source_line_end": 192,
  "registry_ids": [
    "VII.T47"
  ],
  "related_registry_items": [
    {
      "id": "VII.T47",
      "title": "No Forced Stance",
      "url": "/registry/object/VII.T47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L185-L192",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Final.Boundary",
        "url": "/verify/taulib/docs/book-vii-final-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L185-L192",
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

- Module: [TauLib.BookVII.Final.Boundary](/verify/taulib/docs/book-vii-final-boundary/)
- Source path: [`TauLib/BookVII/Final/Boundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L185-L192)
- Source range: L185-L192
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.T47` — No Forced Stance

## Immediate Comment / Docstring

```lean
/-- [VII.T47] No Forced Stance (ch123). ω is undecidable in Reg_D:
    the diagrammatic register cannot force a stance on ω-content.
    Subject-Tool Collapse + bounded witness form ⟹ ω undecidable.

    Three claims:
    (1) ω is not NF-addressable in the standard sense (closure point)
    (2) Subject-Tool Collapse at S_L prevents external standpoint
    (3) BWF excludes unbounded ω-witness

    **Methodological-commitment point**: the theorem establishes
    the boundary of formal verification. It cannot be formally proved
    because proving it would require the very standpoint it denies.
    The structural content is formalized below as
    `no_forced_stance_structure` and `no_forced_stance_structural`;
    the commitment content (the claim that the framework does not
    force a stance here) is recorded as a `Commitment` data value
    `no_forced_stance`, NOT as a `theorem : True := sorry`. -/
```

## Source Excerpt

```lean
structure NoForcedStanceStructure where
  /-- ω not standardly NF-addressable. -/
  omega_non_standard : Bool := true
  /-- Subject-tool collapse prevents external standpoint. -/
  no_external_standpoint : Bool := true
  /-- BWF excludes unbounded ω-witness. -/
  bwf_excludes : Bool := true
  deriving Repr
```
