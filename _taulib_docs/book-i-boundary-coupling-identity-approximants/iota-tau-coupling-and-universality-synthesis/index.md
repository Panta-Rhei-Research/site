---
{
  "projection_kind": "taulib_declaration",
  "title": "iota_tau_coupling_and_universality_synthesis",
  "permalink": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/iota-tau-coupling-and-universality-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.CouplingIdentityApproximants`.",
  "declaration_id": "TauLib.BookI.Boundary.CouplingIdentityApproximants::iota_tau_coupling_and_universality_synthesis",
  "declaration_slug": "iota-tau-coupling-and-universality-synthesis",
  "kind": "theorem",
  "name": "iota_tau_coupling_and_universality_synthesis",
  "module_name": "TauLib.BookI.Boundary.CouplingIdentityApproximants",
  "module_url": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/",
  "source_line_start": 303,
  "source_line_end": 312,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L303-L312",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.CouplingIdentityApproximants",
        "url": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L303-L312",
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

- Module: [TauLib.BookI.Boundary.CouplingIdentityApproximants](/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/)
- Source path: [`TauLib/BookI/Boundary/CouplingIdentityApproximants.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L303-L312)
- Source range: L303-L312
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §6.3 + §5.6 synthesis**: the coupling identity holds at
    the ω-limit, AND the scalar `ι_τ` is universally fixed under
    the structural framework of Wave 13.  Together these realise
    paper's complete structural picture:

    `ι_τ = 2/(π_τ + e_τ)` AND `ι_τ` is invariant under every
    `f ∈ HolEnd_τ(ω)`.

    This structural bridging theorem records the conjunction; its
    two components are Wave 4 (operational coupling) and Wave 13
    (universal fixed scalar, conditional). -/
```

## Source Excerpt

```lean
theorem iota_tau_coupling_and_universality_synthesis
    (g : CrossingPointDefectGerm) (h : IsCrossingPoint g) :
    -- The coupling identity at the ω-limit
    (TauReal.equiv ((Read g).mul (TauReal.pi.add TauReal.e)) TauReal.two) ∧
    -- Wave 13's framework applies (conditional on singleton uniqueness,
    -- unconditional on concrete instances like TorusDefectSystem)
    (TauReal.equiv (Read g) TauReal.iota_tau) :=
  ⟨coupling_identity g h, h.2⟩

end Tau.Boundary
```
