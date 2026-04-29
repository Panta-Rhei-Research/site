---
{
  "projection_kind": "taulib_declaration",
  "title": "science_faith_boundary",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/science-faith-boundary/",
  "summary_short": "`def` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::science_faith_boundary",
  "declaration_slug": "science-faith-boundary",
  "kind": "def",
  "name": "science_faith_boundary",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 511,
  "source_line_end": 518,
  "registry_ids": [
    "VII.P29"
  ],
  "related_registry_items": [
    {
      "id": "VII.P29",
      "title": "Four-Register Convergence at S_L",
      "url": "/registry/object/VII.P29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L511-L518",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Logos.Sector",
        "url": "/verify/taulib/docs/book-vii-logos-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L511-L518",
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

- Module: [TauLib.BookVII.Logos.Sector](/verify/taulib/docs/book-vii-logos-sector/)
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L511-L518)
- Source range: L511-L518
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `VII.P29` — Four-Register Convergence at S_L

## Immediate Comment / Docstring

```lean
/-- [VII.P29] Science-Faith-Boundary commitment.

    Monograph-level claim (Book VII ch. 121): for φ ∈ S_L, all
    four readout functors agree —
    Reg_E(φ) ~ Reg_P(φ) ~ Reg_D(φ) ~ Reg_C(φ).

    Retired from `theorem science_faith_boundary : True := sorry`
    in peer-review-fixes-v1 (2026-04-19) for the same reason as
    `omega_point_theorem` above: `True := sorry` is a performative
    no-op encoding.

    The D-C coincidence is verified elsewhere in Book VII's
    structural proofs; the E and P convergence requires
    Reg_C stance-stability that transcends formal verification
    by framework principle. Structural parts are in
    `TauLib.BookVII.Final.Boundary` as
    `four_register_convergence_structural`; the commitment
    content is recorded here as a `Commitment` data value. -/
```

## Source Excerpt

```lean
def science_faith_boundary : Commitment :=
  { statement := "For φ ∈ S_L, all four readout functors agree: " ++
                 "Reg_E(φ) ~ Reg_P(φ) ~ Reg_D(φ) ~ Reg_C(φ)"
    warrant := "Reg_C stance-stability transcends the structural " ++
               "predicate layer; warrant per VII.T47 (No Forced Stance)"
    registry_id := "VII.P29" }

end Tau.BookVII.Logos.Sector
```
