---
{
  "projection_kind": "taulib_declaration",
  "title": "honest_claim_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/honest-claim-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.BridgeAxiom`.",
  "declaration_id": "TauLib.BookIII.Bridge.BridgeAxiom::honest_claim_check",
  "declaration_slug": "honest-claim-check",
  "kind": "def",
  "name": "honest_claim_check",
  "module_name": "TauLib.BookIII.Bridge.BridgeAxiom",
  "module_url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/",
  "source_line_start": 261,
  "source_line_end": 273,
  "registry_ids": [
    "III.T47"
  ],
  "related_registry_items": [
    {
      "id": "III.T47",
      "title": "Honest Claim Theorem",
      "url": "/registry/object/III.T47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L261-L273",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.BridgeAxiom",
        "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L261-L273",
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

- Module: [TauLib.BookIII.Bridge.BridgeAxiom](/verify/taulib/docs/book-iii-bridge-bridge-axiom/)
- Source path: [`TauLib/BookIII/Bridge/BridgeAxiom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L261-L273)
- Source range: L261-L273
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T47` — Honest Claim Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T47] Honest claim check: every established/tau-effective claim
    passes its check at the given (bound, db). This is UNCONDITIONAL --
    no bridge axiom needed for honest claims. -/
```

## Source Excerpt

```lean
def honest_claim_check (bound db : TauIdx) : Bool :=
  go established_claims (established_claims.length + 1)
where
  go (claims : List ClaimRecord) (fuel : Nat) : Bool :=
    if fuel = 0 then true
    else match claims with
    | [] => true
    | claim :: rest =>
      let passes := claim.check bound db
      -- Scope must be established or tau-effective (not conjectural)
      let honest := claim.scope == .established || claim.scope == .tau_effective
      passes && honest && go rest (fuel - 1)
  termination_by fuel
```
